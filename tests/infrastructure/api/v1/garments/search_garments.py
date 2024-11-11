import pytest
from httpx import AsyncClient

@pytest.mark.anyio
async def test_get_garments(client: AsyncClient):
    response = await client.get("/api/v1/garments/")
    assert response.status_code == 200, f"Expected status 200 asserted"
    assert len(response.json()) > 11000


@pytest.mark.anyio
async def test_get_garments_with_limit(client: AsyncClient):
    response = await client.get("/api/v1/garments/?limit=20&offset=0")
    assert response.status_code == 200, f"Expected status 200 asserted"
    assert len(response.json()) == 20

@pytest.mark.anyio
@pytest.mark.parametrize("search_params, expected_status", [
    ({"product_title": "Shirt", "gender": "M"}, 422),
    ({"product_title": "Shirt", "gender": "men"}, 200),
])
async def test_search_garments(client: AsyncClient, search_params, expected_status):
    response = await client.get("/api/v1/garments/", params=search_params)
    assert response.status_code == expected_status, f"Expected status {expected_status}, got {response.status_code}"

    if response.status_code == 200:
        assert isinstance(response.json(), list), "Expected response to be a list"

@pytest.mark.anyio
@pytest.mark.parametrize("endpoint", ["/api/v1/garments/"])
async def test_rate_limit_exceeded(client: AsyncClient, endpoint):
    for _ in range(2):
        response = await client.get(endpoint)
        assert response.status_code == 200, f"Expected 200 OK for {endpoint}, got {response.status_code}"

    response = await client.get(endpoint)
    assert response.status_code == 429, "Expected 429 Too Many Requests due to rate limiting"