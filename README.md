
# Project Setup and Usage

This project is containerized with Docker, using `docker-compose` to manage service orchestration. Below are the commands to build, run, and test the application, as well as to configure MongoDB indexes and seed test data.

## Prerequisites

- Docker
- Docker Compose

## Initial Setup

### 1. Full Setup

To perform a full setup, including building, running, and creating indexes, use the following, and ignore #2 - #4

```bash
make setup
```

### 2. Build the Docker Images

To build the Docker images without caching:

```bash
make build
```

This will pull all required dependencies and build the images defined in the `docker-compose.yml` file.

### 3. Run the Application

To start the application in detached mode:

```bash
make run
```

The application will start in the background. To follow logs, use `docker-compose logs -f`.

### 4. Set Up MongoDB Indexes

To set up indexes in the MongoDB `intelistyle_db` database:

```bash
make mongo-indexes
```

This command will create indexes on fields such as `brand`, `gender`, `product_title`, `product_categories`, and `price` in the `garments` collection.


This command runs all steps sequentially to get your environment up and running.

## Testing

### Set Up the Test Database

To set up the test database (`test_intelistyle_db`) with sample data for testing purposes:

```bash
make setup-test
```

This command will connect to MongoDB, create the `test_intelistyle_db`, and import sample data into the `garments` collection.

### Run Tests

To run tests on the `garments` API:

```bash
make run-test
```

This command will execute tests located in `tests/infrastructure/api/v1/garments/search_garments.py` inside the FastAPI container.

---

## Notes

- Modify the MongoDB connection string, FastAPI server address, or database names if needed, depending on your local setup.
- Ensure your `docker-compose.yml` file is configured to map any required volumes and expose necessary ports for development and testing.

