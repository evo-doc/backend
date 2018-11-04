import pytest

def test_gethome(client):
    assert client.get('/').status_code == 200
