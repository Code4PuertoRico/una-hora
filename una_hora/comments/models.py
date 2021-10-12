from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from una_hora.core.models import BaseModel


class Comment(BaseModel):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="comments",
        related_query_name="comment",
    )
    text = models.TextField(verbose_name=_("comment text"))

    def __str__(self):
        return f"{self.user}: {self.text}"

    class Meta:
        ordering = ("created_at",)
        verbose_name = _("comment")
        verbose_name_plural = _("comments")
