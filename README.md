# Django Todo Project

## Project Overview

This is a Django-based Todo application that allows users to create, view, and update tasks. The project uses Docker for containerization to simplify development and deployment.

## Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- [Python](https://www.python.org/) (for local development, optional)

## Setup and Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/barbodimani81/todo-app.git
    cd your-repo
    ```

2. **Build and run the Docker containers:**

    ```bash
    docker-compose up --build
    ```

    This command builds the Docker images and starts the containers.

## Usage

- **Access the Admin Interface:** [http://localhost:8000/admin/](http://localhost:8000/admin/)
- **Todo Tasks List:** [http://localhost:8000/todo/tasks/](http://localhost:8000/todo/tasks/)
- **Create a Task:** [http://localhost:8000/todo/](http://localhost:8000/todo/)
- **Task Details:** [http://localhost:8000/todo/tasks/<task_id>/](http://localhost:8000/todo/tasks/<task_id>/)
- **Update a Task:** [http://localhost:8000/todo/tasks/<task_id>/update/](http://localhost:8000/todo/tasks/<task_id>/update/)

## Docker Setup

1. **Dockerfile**: Defines the environment for the Django application.

2. **docker-compose.yml**: Configures the services required to run the application, including the web service and database.

    Example `docker-compose.yml`:

    ```yaml
    version: '3.8'

    services:
      web:
        image: django:latest
        command: python manage.py runserver 0.0.0.0:8000
        volumes:
          - .:/app
        ports:
          - "8000:8000"
        depends_on:
          - db

      db:
        image: postgres:latest
        environment:
          POSTGRES_DB: todo_db
          POSTGRES_USER: user
          POSTGRES_PASSWORD: password
        volumes:
          - pg_data:/var/lib/postgresql/data

    volumes:
      pg_data:
    ```

## URL Configuration

### Main Project `urls.py`

```python
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('todo/', include('todo.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
