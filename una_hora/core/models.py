from uuid import uuid4

from django.db import models


class BaseModel(models.Model):
    """
    An abstract base class model that provides the following fields:
        - id (UUIDField)
        - created_at
        - updated_at
    """

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        get_latest_by = "updated_at"
        ordering = ("-updated_at", "-created_at")
        indexes = [
            models.Index(fields=["-updated_at"]),
            models.Index(fields=["-created_at"]),
        ]
