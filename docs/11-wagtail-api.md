# Wagtail API v2

Wagtail exposes a public, read-only, JSON-formatted API at `/api/v2/`. This document describes how to use it for the blog and other content. See the [official Wagtail API v2 usage guide](https://docs.wagtail.org/en/stable/advanced_topics/api/v2/usage.html) for full reference.

## Endpoints

| Endpoint | Description |
|----------|-------------|
| `/api/v2/pages/` | Pages (blog posts, index pages, etc.) |
| `/api/v2/images/` | Images |
| `/api/v2/documents/` | Documents |

## Response Format

Each listing response contains:

```json
{
  "meta": {
    "total_count": 10
  },
  "items": [
    {
      "id": 1,
      "meta": {
        "type": "blog.BlogPage",
        "detail_url": "http://localhost:8000/api/v2/pages/1/",
        "html_url": "http://localhost:8000/pages/blog/my-post/",
        "slug": "my-post",
        "first_published_at": "2026-02-22T12:00:00Z"
      },
      "title": "My Blog Post",
      "date": "2026-02-22",
      "intro": "Short intro...",
      "body": "<p>Rich text content...</p>"
    }
  ]
}
```

## Blog API

### Page Types

| Type | Purpose |
|------|---------|
| `blog.HomePage` | Root page (structural only) |
| `blog.BlogPage` | Individual blog post |

### Exported Fields (BlogPage)

Fields exposed via `api_fields`:

- `date` — Post date
- `intro` — Short intro (max 250 chars)
- `body` — Rich text (HTML)
- `feed_image` — Optional featured image
- `feed_image_thumbnail` — 600×400 fill rendition (for responsive images)

### Rich Text (body field)

The `body` field returns HTML. Wagtail may include custom elements for internal links and image embeds. For Next.js: use `dangerouslySetInnerHTML` to render, or parse with a library. Alternatively, use `wagtail-grapple` (GraphQL) for pre-rendered HTML.

### List Blog Posts

```http
GET /api/v2/pages/?type=blog.BlogPage&child_of=<HOME_ID>&fields=title,meta,date,intro,body,feed_image_thumbnail&order=-first_published_at
```

**Parameters:**

- `type=blog.BlogPage` — Filter to blog posts only
- `child_of=<ID>` — Only posts under this home page
- `fields=...` — Comma-separated fields to return (required for custom fields)
- `order=-first_published_at` — Newest first

**curl example:**

```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.BlogPage&child_of=2&fields=title,meta,date,intro,body,feed_image_thumbnail&order=-first_published_at"
```

### Single Post by Slug

```http
GET /api/v2/pages/?type=blog.BlogPage&slug=<slug>&fields=*,body
```

**curl example:**

```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.BlogPage&slug=my-first-post&fields=*,body"
```

### Single Post by ID

```http
GET /api/v2/pages/<id>/?fields=*,body
```

**curl example:**

```bash
curl "http://localhost:8000/api/v2/pages/5/?fields=*,body"
```

### Find Home Page ID

Create a site with Home as root in the CMS (`/cms/`), then:

```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.HomePage"
```

Use the `id` from the response as `child_of` when listing posts.

## Pagination

| Parameter | Default | Description |
|-----------|---------|-------------|
| `limit` | 20 | Max items per response (max 20 unless `WAGTAILAPI_LIMIT_MAX` is set) |
| `offset` | 0 | Number of items to skip |

**Example:**

```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.BlogPage&child_of=2&limit=10&offset=20"
```

## Ordering

Use `?order=<field>` for ascending, `?order=-<field>` for descending.

**Examples:**

- `?order=title` — A–Z
- `?order=-first_published_at` — Newest first
- `?order=title,-slug` — Multiple fields

**Random order:**

```bash
curl "http://localhost:8000/api/v2/pages/?type=blog.BlogPage&order=random"
```

Note: `?offset` cannot be used with `order=random`.

## Filtering

| Parameter | Description |
|-----------|-------------|
| `slug` | Exact slug match |
| `child_of` | Direct children of page ID |
| `ancestor_of` | Ancestors of page ID |
| `descendant_of` | Descendants of page ID |
| `site` | Filter by site hostname (e.g. `?site=localhost`) |

**Example:**

```bash
curl "http://localhost:8000/api/v2/pages/?slug=about"
```

## Fields

| Parameter | Description |
|-----------|-------------|
| `?fields=field1,field2` | Add fields to response |
| `?fields=*` | All available fields |
| `?fields=-title` | Remove a default field |
| `?fields=_,title` | Only title (underscore removes all defaults) |

**Nested fields:**

```bash
curl "http://localhost:8000/api/v2/pages/5/?fields=body,feed_image(width,height)"
```

## Search

Full-text search via `?search=`:

```bash
curl "http://localhost:8000/api/v2/pages/?search=keyword"
```

**Search operator** (`?search_operator=`):

- `or` — At least one term must match (default with Elasticsearch)
- `and` — All terms must match (default with database backend)

**Example with ordering:**

```bash
curl "http://localhost:8000/api/v2/pages/?search=research&order=-first_published_at&search_operator=and"
```

## Detail View

Retrieve a single object by ID:

```bash
curl "http://localhost:8000/api/v2/pages/5/"
curl "http://localhost:8000/api/v2/images/1/"
curl "http://localhost:8000/api/v2/documents/1/"
```

## Find by HTML Path

Resolve a page by its URL path (returns 302 redirect or 404):

```bash
curl -I "http://localhost:8000/api/v2/pages/find/?html_path=/"
curl -I "http://localhost:8000/api/v2/pages/find/?html_path=/blog/my-post/"
```

## Default Page Fields

All page responses include:

- `id` — Unique ID
- `meta.type` — Model type (e.g. `blog.BlogPage`)
- `meta.detail_url` — API detail URL
- `meta.html_url` — Frontend URL (if applicable)
- `meta.slug` — URL slug
- `meta.first_published_at` — Publication timestamp
- `title` — Page title

## Images and Documents

**Images** include `title`, `width`, `height`, `meta.tags`, and `meta.download_url`.

**Documents** include `title`, `meta.tags`, and `meta.download_url`.

```bash
curl "http://localhost:8000/api/v2/images/"
curl "http://localhost:8000/api/v2/documents/"
```

## CORS

CORS is configured for Next.js (`http://localhost:3000`, `http://127.0.0.1:3000`). Override via `CORS_ALLOWED_ORIGINS` in `.env`.
