from django.db import models
from wagtail.api import APIField
from wagtail.fields import RichTextField
from wagtail.images import get_image_model_string
from wagtail.models import Page


class HomePage(Page):
    """
    Minimal root page. Only BlogIndexPage can be created under it.
    Required for Wagtail's site structure; not used by the Next.js API.
    """

    subpage_types = ["blog.BlogIndexPage"]
    parent_page_types = ["wagtailcore.Page"]

    # Keep body for backwards compatibility with existing migration
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        "body",
    ]


class BlogIndexPage(Page):
    """Index page that lists blog posts. Create one under Home in the admin."""

    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        "intro",
    ]

    subpage_types = ["blog.BlogPage"]
    parent_page_types = ["blog.HomePage"]

    api_fields = [
        APIField("intro"),
    ]


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
    parent_page_types = ["blog.BlogIndexPage"]

    api_fields = [
        APIField("date"),
        APIField("intro"),
        APIField("body"),
        APIField("feed_image"),
    ]
