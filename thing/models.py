import uuid
from django.db import models


class Base(models.Model):
    """
    Base Model  Class with UUID identification
    """
    class Meta:
        abstract = True
        ordering = [
            'order',
            '-modified_date',
            'name',
        ]

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4, editable=False,
        help_text="""Base ID UUID field"""
    )
    name = models.CharField(
        max_length=64,
        blank=True,
        help_text="""The base name field"""
    )
    desc = models.TextField(
        blank=True,
        help_text="""The base desc field"""
    )
    attrib = models.TextField(
        blank=True,
        help_text="""The base attrib field"""
    )
    order = models.IntegerField(
        default=0,
        help_text="""Base Order Field"""
    )
    created = models.DateTimeField(
        auto_now_add=True
    )
    modified = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.name
