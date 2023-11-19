from flask import Flask
import pytest

@pytest.fixture
def client():
    app = Flask(__name__)
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert b'Hello' in response.data

def test_aboutus(client):
    response = client.get('/aboutus')
    assert b'About Us' in response.data
