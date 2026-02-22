# Deployment

## Docker

- Dockerfile for the API service
- docker-compose for local and production-like setups

## Environment Variables

- See `.env.example` for required variables
- Production: use `.env.production.example` or equivalent as reference
- Never commit secrets; use env vars or secrets manager

## Registries

- Use public registries (Docker Hub, etc.) for base images
- Document any private registry requirements here
