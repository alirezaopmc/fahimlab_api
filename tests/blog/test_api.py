"""Integration tests for Wagtail blog API."""

import pytest
from wagtail.models import Page, Site

from apps.blog.models import BlogIndexPage, BlogPage, HomePage


@pytest.fixture
def blog_index_id(db):
    """Create Wagtail page tree and return blog index ID for child_of queries."""
    root = Page.get_first_root_node()
    Site.objects.create(
        hostname="testserver",
        root_page=root,
        is_default_site=True,
        site_name="testserver",
    )
    home = HomePage(title="Home", slug="home-itest")
    root.add_child(instance=home)
    blog_index = BlogIndexPage(title="Blog", slug="blog-itest")
    home.add_child(instance=blog_index)
    post = BlogPage(
        title="Test Post",
        slug="test-post",
        date="2026-02-22",
        intro="Short intro",
        body="<p>Body content</p>",
    )
    blog_index.add_child(instance=post)
    return blog_index.id


def test_list_blog_posts_returns_expected_structure(client, blog_index_id):
    """List blog posts returns 200 with meta, items, and expected fields."""
    response = client.get(
        f"/api/v2/pages/?type=blog.BlogPage&child_of={blog_index_id}"
        "&fields=title,date,intro,body,feed_image_thumbnail"
        "&order=-first_published_at"
    )
    assert response.status_code == 200, response.content.decode()
    data = response.json()
    assert "meta" in data
    assert "items" in data
    items = data["items"]
    assert len(items) >= 1
    post = items[0]
    assert "title" in post
    assert "date" in post
    assert "intro" in post
    assert "body" in post
    assert "meta" in post


def test_single_post_by_slug(client, blog_index_id):
    """Single post by slug returns 200 with expected fields."""
    response = client.get(
        "/api/v2/pages/?type=blog.BlogPage&slug=test-post&fields=title,date,intro,body"
    )
    assert response.status_code == 200, response.content.decode()
    data = response.json()
    assert "items" in data
    items = data["items"]
    assert len(items) == 1
    post = items[0]
    assert post["title"] == "Test Post"
    assert post["intro"] == "Short intro"
    assert "body" in post
