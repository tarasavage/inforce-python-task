# Inforce Python Task

This project is an internal service for employees to help them make a decision on where to have lunch. It provides functionality for restaurants to upload menus, employees to vote for menus, and retrieving the current day's menu and voting results.

## Installation and Setup

To run the system, follow the steps below:

### Prerequisites

- Docker and Docker Compose installed on your machine.

1. Clone the repository:

```bash
git clone <repository-url>
```

2. Copy the `.env.sample` file and create a new file named `.env`. Populate the `.env` file with all the required data (API keys, database credentials, etc.).

3. Build and run the application using Docker Compose:

```bash
docker-compose up --build
```

4. Create a superuser for accessing the Django admin site:

```bash
docker-compose exec web python manage.py createsuperuser
```

5. Access the API in your web browser at `http://localhost:8000/`.

## API Endpoints

### Authentication

- `POST /api/user/register/`: Register a new user.
- `GET /api/user/me/`: Get the authenticated user's details.
- `POST /api/user/token/`: Obtain an access and refresh token.
- `POST /api/user/token/refresh/`: Refresh an access token.
- `POST /api/user/token/verify/`: Verify an access token.

### Restaurant URLs

- `POST /api/restaurant/create/`: Create a new restaurant.
- `POST /api/restaurant/menu/create/`: Create a menu for a restaurant.
- `GET /api/restaurant/menu/list/`: Get the list of menus for the current day.
- `POST /api/restaurant/{restaurant_id}/vote/`: Vote for a menu of a specific restaurant.
- `GET /api/restaurant/menu/winner/`: Get the highest voted menu of the day (admin-only).

### Menu

- `GET /api/restaurant/menu/list/`: Get the current day's menu.


### API Documentation

- `GET /api/doc/`: API documentation in JSON format.
- `GET /api/doc/swagger/`: Swagger UI for interactive API documentation.

## Running Tests

To run the tests, execute the following command:

```bash
docker-compose exec web pytest
```

## Code Quality

This project adheres to the PEP 8 style guide. To check the code quality, you can run flake8 using the command:

```bash
docker-compose exec web flake8
```
