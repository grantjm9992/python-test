
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

## Prometheus and Grafana Setup

Prometheus and Grafana are included in the setup to monitor and visualize the metrics of the FastAPI application.

### 1. Prometheus
   Prometheus is configured to scrape metrics from the FastAPI application. The configuration file prometheus.yml is mapped in the docker-compose.yml file and sets up scraping from the FastAPI container.

Key Points:
Prometheus scrapes the /metrics endpoint exposed by FastAPI.
The prometheus.yml file should be configured properly for FastAPI.

### 2. Grafana
   Grafana is included to visualize the Prometheus metrics. After running the docker-compose setup, you can access Grafana at http://localhost:3000 (default login: admin / admin).

Grafana Data Source Configuration:
Grafana will automatically detect Prometheus as the data source.
In Grafana, go to Configuration > Data Sources and verify that Prometheus is set up correctly with the URL http://prometheus:9090.
### 3. Visualizing Metrics
   Once Prometheus and Grafana are up and running, you can create dashboards in Grafana to monitor your FastAPI application. Grafana can automatically create default dashboards, or you can create custom ones to visualize application performance metrics like request rate, response times, etc.

### To access Grafana dashboards:

Open a web browser and go to http://localhost:3000/d/_eX4mpl3/fastapi-dashboard?from=now-5m&to=now&refresh=5s.
Log in with the default credentials (username: admin, password: admin).
Create or import more dashboards to visualize the metrics.

---


## Notes

- Modify the MongoDB connection string, FastAPI server address, or database names if needed, depending on your local setup.
- Ensure your `docker-compose.yml` file is configured to map any required volumes and expose necessary ports for development and testing.

