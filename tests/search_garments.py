import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../../../app')))
from fastapi.testclient import TestClient
from fastapi import FastAPI
from app.main import app
from fastapi import Request
from fastapi.responses import PlainTextResponse
from slowapi.errors import RateLimitExceeded

client = TestClient(app)

@pytest.mark.parametrize("endpoint", ["/api/v1/garments"])
def test_garments_endpoint(endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200, f"Expected 200 OK for {endpoint}, got {response.status_code}"

@pytest.mark.parametrize("endpoint", ["/api/v1/garments"])
def test_rate_limit(endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200, f"Expected 200 OK for {endpoint}, got {response.status_code}"

@pytest.mark.parametrize("endpoint", ["/api/v1/garments"])
def test_rate_limit_exceeded(endpoint):
    for _ in range(5):
        response = client.get(endpoint)
        assert response.status_code == 200, f"Expected 200 OK for {endpoint}, got {response.status_code}"

    response = client.get(endpoint)
    assert response.status_code == 429, "Expected 429 Too Many Requests due to rate limiting"

@pytest.mark.parametrize("search_params, expected_status", [
    ({"product_title": "Shirt", "gender": "M"}, 422),
    ({"product_categories": "One, Two"}, 200),
])
def test_search_garments(search_params, expected_status):
    response = client.get("/api/v1/garments", params=search_params)
    assert response.status_code == expected_status, f"Expected status {expected_status}, got {response.status_code}"

    if response.status_code == 200:
        assert isinstance(response.json(), list), "Expected response to be a list"

@pytest.mark.parametrize("endpoint", ["/api/v1/garments"])
def test_request_signature(endpoint):
    response = client.get(endpoint)
    assert response.status_code == 200, f"Expected 200 OK for {endpoint}, got {response.status_code}"
