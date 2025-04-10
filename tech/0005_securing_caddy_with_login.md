---
title: 0005_securing_caddy_with_login
author: Wynand Gouws
date: 2025-03-09 16:45:04
public: true
---

# Title: Securing web apps with Caddy and Authelia in Docker Compose: an opinionated, practical, and minimal production-ready login portal guide

## Status: Draft

- Note that most of this is taken from this[^1] website

## Theory

- Will hand off authentication and authorisation to a seperate service
  - Just makes it easier
  - Allows configuring security ONCE for multiple caddy servers if need be

### The Stack

- The stack is basically:
  - Caddy
  - Authelia
    - Redis to store login sessions
    - Postgres as a database to handle stored credentials

### Secrets

- All needed secrets need to be generated freshly and stored into files
  - allows keeping the secrets out of the Authelia container in plain-text
- All of the above are recommended to be 64+ character long random alphanumeric strings, and Authelia’s documentation advises how these should be generated
- Secrets that need to be generated:
  - JWT Secret
  - Session Secret
  - Storage encryption key
  - Storage password
  - Redis password

## Implimentation

### Setting up the secrets

- Secrets will be stored in `docker_data` as per usual, but in a seperate folder named `secrets`
- Run the following commands

```bash
tr -cd '[:alnum:]' < /dev/urandom | fold -w 64 | head -n 1 | tr -d '\n' > /home/wynand/docker_data/secrets/AUTHELIA_JWT_SECRET
tr -cd '[:alnum:]' < /dev/urandom | fold -w 64 | head -n 1 | tr -d '\n' > /home/wynand/docker_data/secrets/AUTHELIA_SESSION_SECRET
tr -cd '[:alnum:]' < /dev/urandom | fold -w 64 | head -n 1 | tr -d '\n' > /home/wynand/docker_data/secrets/AUTHELIA_STORAGE_PASSWORD
tr -cd '[:alnum:]' < /dev/urandom | fold -w 64 | head -n 1 | tr -d '\n' > /home/wynand/docker_data/secrets/AUTHELIA_STORAGE_ENCRYPTION_KEY
tr -cd '[:alnum:]' < /dev/urandom | fold -w 64 | head -n 1 | tr -d '\n' > /home/wynand/docker_data/secrets/AUTHELIA_REDIS_PASSWORD
```

- We also want to send emails to us for failed logins etc
  - Need to paste the SMPT password into `/home/wynand/docker_data/secrets/AUTHELIA_SMTP_PASSWORD`

## References

[^1]: Caddy Community, Securing web apps with Caddy and Authelia in Docker Compose: an opinionated, practical, and minimal production-ready login portal guide - Wiki - Caddy Community. Published 2023-09-18. Accessed 2025-03-09. Available from: <https://caddy.community/t/securing-web-apps-with-caddy-and-authelia-in-docker-compose-an-opinionated-practical-and-minimal-production-ready-login-portal-guide/20465>
