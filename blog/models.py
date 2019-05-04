from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.search import index

class Post(Page):
    summary = models.TextField(blank=True)
    body = RichTextField(blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('summary', classname="full"),
        FieldPanel('body', classname="full"),
    ]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
