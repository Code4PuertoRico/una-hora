from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_fsm import FSMField, TransitionNotAllowed, transition

from una_hora.core.models import BaseModel

UserModel = get_user_model()


class Meeting(BaseModel):
    class MeetingState(models.TextChoices):
        """
        requested:
            A meeting with a mentor that was requested by mentee.

        confirmed:
            A meeting that was requested by a mentee and later accepted
            by the meeting's mentor.

        canceled:
            A meeting that was either requested or confirmed and
            then CANCELED by either the mentor or mentee.

        expired:
            A meeting that was requested by a mentee and was not
            confirmed by the mentor in time.
        """

        REQUESTED = "REQUESTED", _("requested")
        CONFIRMED = "CONFIRMED", _("confirmed")
        CANCELED = "CANCELED", _("canceled")
        EXPIRED = "EXPIRED", _("expired")

    mentor = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="meetings_as_mentor",
        related_query_name="mentor_meeting",
        verbose_name=_("mentor"),
    )
    mentee = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="meetings_as_mentee",
        related_query_name="mentee_meeting",
        verbose_name=_("mentee"),
    )
    canceled_by = models.ForeignKey(
        UserModel,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="+",
        verbose_name=_("canceled by user"),
    )
    state = FSMField(default=MeetingState.REQUESTED, verbose_name=_("meeting state"))
    message = models.TextField(blank=True, verbose_name=_("meeting request message"))
    datetime = models.DateTimeField(verbose_name=_("meeting datetime"))

    class Meta:
        ordering = ("-datetime",)
        verbose_name = _("meeting")
        verbose_name_plural = _("meetings")

    def __str__(self):
        return f"Meeting ({self.id}) between {self.mentor} and {self.mentee}"

    @transition(
        field=state,
        source=MeetingState.REQUESTED,
        target=MeetingState.CONFIRMED,
    )
    def flag_confirmed(self, confirmed_by):
        if self.mentor != confirmed_by:
            raise TransitionNotAllowed

    @transition(
        field=state,
        source=[MeetingState.REQUESTED, MeetingState.CONFIRMED],
        target=MeetingState.CANCELED,
    )
    def flag_canceled(self, canceled_by):
        if canceled_by not in [self.mentor, self.mentee]:
            raise TransitionNotAllowed

        self.canceled_by = canceled_by

    @transition(field=state, source=MeetingState.REQUESTED, target=MeetingState.EXPIRED)
    def flag_expired(self):
        pass
