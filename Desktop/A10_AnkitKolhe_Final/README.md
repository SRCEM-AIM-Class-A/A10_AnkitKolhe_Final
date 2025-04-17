# Web Applications with Flask, Django, and Docker Compose

This project demonstrates building web applications using Flask and Django, containerized using Docker Compose.

## Project Structure

- `flask_app/`: A simple Flask application with form handling
- `django_app/`: A Django application with database integration and admin panel
- `docker-compose.yml`: Configuration to run both applications in containers

## Requirements

- Docker and Docker Compose

## Getting Started

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Build and start the containers:
   ```
   docker-compose up --build
   ```

3. Access the applications:
   - Flask application: http://localhost:5000
   - Django application: http://localhost:8000
   - Django admin panel: http://localhost:8000/admin
     - Username: admin
     - Password: adminpassword

## Features

### Flask Application
- Homepage with a "Hello, World!" message
- Form page that accepts user's name and age
- Error handling for invalid inputs

### Django Application
- Item listing on the homepage
- Form to add new items
- Admin panel for managing items

## Stopping the Applications

To stop the running containers:
```
docker-compose down
```