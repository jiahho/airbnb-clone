from django.db import models
from . import managers


class TimeStampedModel(models.Model):

    """Tieme Stamped Model"""

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    objects = managers.CustomModelManage()

    class Meta:
        abstract = True
