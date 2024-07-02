# Stocks-REST-API

This project is a FastAPI application that provides a REST API for managing stock information. The application includes endpoints for retrieving stock data from an external API (Polygon.io) and updating stock amounts. It also logs events and orders into a PostgreSQL database.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Docker](#docker)
- [Endpoints](#endpoints)
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

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
