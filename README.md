# Django Todo App

This is a simple Todo application built with Django, utilizing Class-Based Views (CBV) for its functionality. The app allows users to register, log in, and manage their tasks.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Docker Setup](#docker-setup)
- [URL Configuration](#url-configuration)
- [License](#license)

## Features

- User registration and login
- Create, view, update, and delete tasks
- Admin interface for managing users and tasks
- Responsive and user-friendly interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/barbodimani81/event.git
   cd event
   
2. Docker Setup:
   ```bash
   docker-compose up --build

Main URLs

	•	Admin Panel: /admin/
	•	User Login: / (GET: Show login form)
	•	User Registration: /register/ (GET: Show registration form)
	•	User Logout: /logout/

Todo URLs

	•	Task List: /todo/tasks/
	•	Create Task: /todo/ (POST: Create a new task)
	•	Task Detail: /todo/tasks/<int:pk>/ (GET: View task details)
	•	Update Task: /todo/tasks/<int:pk>/update/ (POST: Update a task)
	•	Delete Task: /todo/tasks/<int:pk>/delete/ (POST: Delete a task)

You can access these URLs by navigating to http://localhost:8000 followed by the route (e.g., http://localhost:8000/register/ for registration).