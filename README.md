# Stocks-REST-API

This project is a FastAPI application that provides a REST API for managing stock information. The application includes endpoints for retrieving stock data from an external API (Polygon.io) and updating stock amounts. It also logs events and orders into a PostgreSQL database.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Installing and Running the Application using Docker](#docker)
- [Endpoints](#endpoints)
- [License](#license)

## Features
- Retrieve stock data from Polygon.io.
- Update stock amounts.
- Log events and orders.
- PostgreSQL database integration.

## Requirements
- Python 3.5 or above
- PostgreSQL 14
- Docker (optional, for containerized deployment)

## Installing and Running the Application using Docker

### Using Docker Compose

**Build and run the containers:**

    ```sh
    docker compose up --build
    ```

## API

**The API documentation can be found at:**

    Open your browser and navigate to `http://127.0.0.1:8000/docs`.

### Retrieve Stock Data
- **GET /stock/{symbol}**
    - Retrieves stock data for the given symbol. The data is fetched from Polygon.io and stored in a database.
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
