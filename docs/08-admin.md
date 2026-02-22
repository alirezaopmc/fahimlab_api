# Admin

## URLs

| URL | Description |
|-----|-------------|
| `/admin/` | Django admin |
| `/cms/` | Wagtail CMS admin |

## Wagtail CMS Setup

1. **Create superuser** (first time only):
   ```bash
   uv run python manage.py createsuperuser
   ```

2. **Log in** at http://localhost:8000/cms/

3. **Create blog structure**:
   - Under **Home**, add a child page → choose **Blog index page**
   - Give it a title (e.g. "Blog") and slug (e.g. "blog")
   - Publish
   - Under the Blog index, add child pages → choose **Blog page**
   - Fill in date, intro, body, optional feed image
   - Publish

4. **Get blog index ID** for the API:
   ```bash
   curl "http://localhost:8000/api/v2/pages/?type=blog.BlogIndexPage"
   ```
   Use the `id` from the response as `child_of` when fetching posts.

## Page Types

| Type | Parent | Purpose |
|------|--------|---------|
| HomePage | Root | Site root; only Blog index can be added |
| BlogIndexPage | HomePage | Blog listing page |
| BlogPage | BlogIndexPage | Individual blog post |

## Permissions

- **Django admin**: Superuser/staff permissions
- **Wagtail**: Page-level permissions (edit, publish, etc.)
- Custom permissions per app as needed

## Roles

Define roles and permissions as admin workflows are implemented: superuser, staff, content editors, etc.
