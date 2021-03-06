# -*- coding: utf-8 -*-
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.snippets.models import register_snippet


@register_snippet
class EmbedCodeSnippet(models.Model):
    """Return rendered embed code."""

    description = models.CharField(max_length=255)
    url = models.URLField(null=True, blank=True)
    embed_code = models.TextField()

    panels = [FieldPanel("description"), FieldPanel("url"), FieldPanel("embed_code")]

    def __str__(self):
        return self.description
