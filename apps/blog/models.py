from django.db import models
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.images.api.fields import ImageRenditionField
from wagtail.models import Page


class HomePage(Page):
    """
    Minimal root page. BlogPage can be created directly under it.
    Required for Wagtail's site structure; not used by the API.
    """

    subpage_types = ["blog.BlogPage"]
    parent_page_types = ["wagtailcore.Page"]


class BlogPage(Page):
    """Individual blog post."""

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    feed_image = models.ForeignKey(
        get_image_model_string(),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    content_panels = Page.content_panels + [
        "date",
        "intro",
        "body",
        "feed_image",
    ]

    subpage_types = []
    parent_page_types = ["blog.HomePage"]

    api_fields = [
        APIField("date"),
        APIField("intro"),
        APIField("body"),
        APIField("feed_image"),
        APIField(
            "feed_image_thumbnail",
            serializer=ImageRenditionField("fill-600x400", source="feed_image"),
        ),
    ]
