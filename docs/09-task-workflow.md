# Task Workflow — AI IDE Execution

## How AI IDEs (e.g., Cursor) Should Run Tasks

1. **Start**: Use Cursor's on-the-fly plan feature before coding (no plan files created in the project)
2. **Branch first**: Switch to a new branch with conventional naming *before* writing code. Use `feat/area/description` or `fix/area/description` (e.g., `feat/blog/wagtail`, `fix/auth/session-handling`). Never work on `main`/`dev` directly.
3. **Follow**: Use the embedded task template(s) and plan structure in this document
4. **Execute**: Work through phases; mark progress in the on-the-fly plan
5. **Tests**: For logic or feature code, include integration tests. See [docs/10-testing.md](10-testing.md). Tests run on approved PRs via CI; see [docs/12-cicd.md](12-cicd.md).
6. **Commit**: Commit each portion of related files atomically with conventional messages (e.g., `feat(people): add Person model and migrations`, `feat(people): add repositories and services`)
7. **Finish**: Update relevant docs in `docs/` when the task completes
8. **No automatic commits**: Do not commit changes unless the user explicitly requests it. The user retains responsibility for final commits.

---

## Git Workflow

- **Branch naming**: `feat/area/short-description` (e.g., `feat/blog/wagtail`) or `fix/area/short-description` (e.g., `fix/auth/session-handling`)
- **Commit responsibility**: The AI must not commit changes unless the user explicitly requests it. Commits remain the user's responsibility.
- **Commits**: Atomic and conventional — one logical change per commit. Examples:
  - `feat(people): add Person model`
  - `fix(auth): correct session handling`
  - `docs(api): update endpoint list`

---

## Plan Structure (Battle-Tested)

Use this structure when creating on-the-fly plans in Cursor:

```markdown
# Plan: [Task Title]
Status: Draft | In Progress | Completed

## Context
[Why this task exists; what problem it solves; relevant background]

## Scope
**In scope:** [What will be done]
**Out of scope:** [What won't be done; explicit boundaries]

## Goals
[Explicit success criteria; what "done" means]

## Implementation
[Ordered phases — adapt per task type]

1. [Phase 1 — e.g., Define scope and models]
2. [Phase 2 — e.g., Setup Django app and configs]
3. [Phase 3 — e.g., Implement integration tests]
4. [Phase 4 — e.g., Implement repositories]
5. [Phase 5 — e.g., Implement services]
6. [Phase 6 — e.g., Implement API layer]

## Acceptance Criteria
- [ ] [Criterion 1]
- [ ] [Criterion 2]

## Doc Updates
[Which docs to update when done — e.g., 02-architecture, 03-database, 04-api, 10-testing]

## Risks and Blockers
[Known issues, dependencies, or things that could go wrong]

## Notes
[Decisions, rationale, or follow-ups]
```

---

## Task Template: Add Django Module

| Phase | Action |
|-------|--------|
| 1 | Define scope, models, API surface |
| 2 | Setup Django app (`uv run python manage.py startapp`), add to INSTALLED_APPS, wire URLs |
| 3 | Implement integration tests (API tests; see [docs/10-testing.md](10-testing.md)) |
| 4 | Implement repositories (`{app}/repositories.py`; ORM preferred; parameterized SQL if raw) |
| 5 | Implement services (`{app}/services.py`) |
| 6 | Implement DRF viewsets and serializers |
