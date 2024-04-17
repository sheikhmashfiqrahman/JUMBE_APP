import pytest
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
    app.config['Limiter_ENABLED'] = True 

    # Apply the routes configuration
    configure_routes(app)

    yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_rate_limit(client):
    limit = 300  
    url = '/api/jumble/1'
    for i in range(limit):
        response = client.post(url, json={"message": "hello"})
        assert response.status_code == 200
# test        
def test_rate_limit_over(client):
    url = '/api/jumble/1'
    # slightly above to see the blocking
    limit = 310  
    url = '/api/jumble/1'
    for i in range(limit):
        response = client.post(url, json={"message": "hello"})
        if i > 300:
            assert response.status_code == 429
            assert response.json == {'error': 'Too many requests'}
            break
