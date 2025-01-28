
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello(client):
    rv = client.get('/')
    assert rv.data == b'Hello, World!'

def test_test_route(client):
    rv = client.get('/test')
    assert rv.data == b'Test route'