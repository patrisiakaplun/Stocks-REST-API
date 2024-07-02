# Stocks-REST-API

This project is a FastAPI application that provides a REST API for managing stock information. The application includes endpoints for retrieving stock data from an external API (Polygon.io) and updating stock amounts. It also logs events and orders into a PostgreSQL database.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Endpoints](#endpoints)
- [Docker](#docker)
- [License](#license)

## Features
- Retrieve stock data from Polygon.io.
- Update stock amounts.
- Log events and orders.
- PostgreSQL database integration.

## Requirements
- Python 3.11.5
- PostgreSQL 14
- Docker (optional, for containerized deployment)

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/patrisiakaplun/Stocks-REST-API.git
    cd Stocks-REST-API
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

    Create a `.env` file in the root directory with the following content:

    ```env
    DATABASE_URL=postgresql://user1:user1@localhost/stocks_db
    POLYGON_API_KEY=your_polygon_api_key_here
    ```

5. **Set up the database:**

    Ensure PostgreSQL is running and create the necessary database:

    ```sh
    psql -U user1 -h localhost
    CREATE DATABASE stocks_db;
    ```

6. **Run database migrations:**

    ```sh
    alembic upgrade head
    ```

## Running the Application

1. **Run the FastAPI application:**

    ```sh
    uvicorn app.main:app --reload
    ```

2. **Access the API documentation:**

    Open your browser and navigate to `http://127.0.0.1:8000/docs` to view the automatically generated API documentation.

## Endpoints

### Retrieve Stock Data
- **GET /stock/{symbol}**
    - Retrieves stock data for the given symbol from the database. If not found, fetches from Polygon.io and stores it in the database.
    - **Response:** JSON object with stock data.

### Update Stock Amount
- **POST /stock/{symbol}**
    - Updates the amount of stock for the given symbol.
    - **Request Body:**
      ```json
      {
          "amount": 5
      }
      ```
    - **Response:** JSON object with a message confirming the update.

## Docker

### Using Docker Compose

1. **Build and run the containers:**

    ```sh
    docker-compose up --build
    ```

2. **Access the API documentation:**

    Open your browser and navigate to `http://127.0.0.1:8000/docs`.

### Running with Docker

1. **Build the Docker image:**

    ```sh
    docker build -t my-fastapi-app .
    ```

2. **Run the Docker container:**

    ```sh
    docker run -d -p 8000:8000 my-fastapi-app
    ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
