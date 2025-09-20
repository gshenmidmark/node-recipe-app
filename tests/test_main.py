import pytest
from src.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_cities_spain(client):
    response = client.get('/countries/spain/cities')
    assert response.status_code == 200
    data = response.get_json()
    assert data == {
        "country": "spain",
        "cities": ["Madrid", "Barcelona", "Valencia"]
    }
