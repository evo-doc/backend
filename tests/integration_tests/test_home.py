

def test_gethome(client):
    """
    Basic test if our app even runs
    """
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == "Hello there"
