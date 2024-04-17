import pytest
from app.services import jumble
from flask import Flask
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from app.routes import configure_routes  # Make sure to adapt the import path as necessary

@pytest.fixture
def app():
    # Create a new Flask instance
    app = Flask(__name__)
    limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["300 per minute"]
   
    )
    # Configure the application for testing
    app.config['TESTING'] = True
    app.config['DEBUG'] = True
    app.config['LIMITEr_ENABLED'] = False  

    # Apply the routes configuration
    configure_routes(app)

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_api_jumble(client):
    # Test with valid data
    response = client.post('/api/jumble/1', json={"message": "hello"})
    assert response.status_code == 200
    assert response.json == {'jumbled': 'ifmmp'}  # Expected output after shifting "hello" by 1

    # Test with empty message
    response = client.post('/api/jumble/1', json={"message": ""})
    assert response.status_code == 400
    assert response.json == {'error': 'No message provided'}

    # Test with no message field
    response = client.post('/api/jumble/1', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'No message provided'}

    # Test with non-JSON payload
    response = client.post('/api/jumble/1', data="This is not JSON")
    assert response.status_code == 415  

    # Test with very high shift amount
    response = client.post('/api/jumble/100', json={"message": "abc"})
    assert response.status_code == 200
    # Check if the shift is correctly wrapped around the alphabet
    assert response.json == {'jumbled': 'wxy'} 

