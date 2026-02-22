# Overview

## Project Goals

Ali Fahim Laboratory API (Lab Lobby API) provides a public-facing portal for lab information. The API serves:

- Lab members (people)
- Publications
- Projects
- Blog content
- Application/contact workflows

Admins manage content via Django admin and Wagtail CMS.

## Audience

- **Public consumers**: Frontend applications (e.g., Next.js) that display lab information
- **Admins**: Lab staff who manage content via admin interfaces

## Stack

- **Backend**: Django 6, Django REST Framework, Wagtail CMS
- **Frontend (consumers)**: Next.js (separate repo)
- **Package manager**: uv
- **Database**: PostgreSQL (production), SQLite (development)
- **Storage**: S3 for media and uploads
