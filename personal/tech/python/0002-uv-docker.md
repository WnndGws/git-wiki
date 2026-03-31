---
title: 0002-uv-docker
author: Wynand Gouws
date: 2026-02-07 12:55:00
public: True
---

# Docker and uv

## Steps

0. ssh into server
1. cd into `/opt/stacks/uv
2. clone the repo into the folder and cd into it
3. repo should already have `docker/` and `src/` folders.
   if not, create them

    0.0 Dockerfile and compose.yaml should look like a version of the one below

4. Run the command to build `docker compose -f docker/compose.yaml up --build`

## Files

```compose.yaml
services:
  project:
    container_name: project
    build:
      context: ../
      dockerfile: docker/Dockerfile
    volumes:
      - ../:/home/project/project
    ports:
      - 8010:8000
    develop:
        watch:
            # Rebuild the image if dependencies change by checking uv.lock
            - action: rebuild
            path: ./uv.lock
```

```Dockerfile

FROM python:3.14

ENV USER=project \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    UV_PROJECT_ENVIRONMENT=/usr/local

RUN apt-get update && apt-get install --no-install-recommends -y \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    && useradd -m -s /bin/bash $USER

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV APP_DIR=/home/$USER/src

WORKDIR $APP_DIR

COPY src $APP_DIR

ENV PYTHONPATH=$APP_DIR

RUN chown -R "$USER":"$USER" $APP_DIR
USER $USER

CMD ["python", "src/path/to/python/file"]
```

# References

* <https://medium.com/@benitomartin/deep-dive-into-uv-dockerfiles-by-astral-image-size-performance-best-practices-5790974b9579>
* <https://medium.com/@shaliamekh/python-package-management-with-uv-for-dockerized-environments-f3d727795044>
