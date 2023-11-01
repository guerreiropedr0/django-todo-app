# Django HTMX Todo List App

This repository contains a simple Todo list application built using Django and HTMX. The purpose of this project was to introduce me to Python, Django, and HTMX by creating a basic yet functional Todo list.

## Features

- **Todo Creation**: Users can create new tasks to add to the list.
- **Todo Completion**: Mark tasks as completed.
- **Todo Deletion**: Remove tasks from the list.
- **Todo Update**: User can edit existing tasks.
- **Dynamic Updates**: HTMX is used to provide dynamic updates to the user interface without full-page reloads, resulting in a smoother user experience.

## Technologies Used

- **Python**: Backend programming language.
- **Django**: Web framework for building the application.
- **HTMX**: Library for creating web applications with seamless AJAX interactions.

## Installation

To run this application locally, follow these steps:

1. Clone this repository: 
   ```bash
   git clone https://github.com/guerreiropedr0/django-todo-app
   ```

2. Navigate to the project directory:
   ```bash
   cd django-todo-app
   ```

3. Apply migrations:
   ```bash
   python manage.py migrate
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Access the application in your web browser at http://localhost:8000.

## Acknowledgements
[Django Documentation](https://docs.djangoproject.com/en/4.2/)

[HTMX Documentation](https://htmx.org/docs/)