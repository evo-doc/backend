import pytest


test_data_422 = [
    {},
    {'email': ''},
    {'email': '', 'password': ''},
]

test_data_400 = [
    (
        {'email': 'test', 'password': 'test', 'username': 'test'},
        {
            'invalid': ['email', 'password'],
            'message': 'Sign up data are invalid or non-unique.'
        }
    ),
    (
        {'email': 'test@example.com', 'password': '', 'username': ''},
        {
            'invalid': ['username', 'password'],
            'message': 'Sign up data are invalid or non-unique.'
        }
    ),
    (
        {'email': '@example.com', 'password': 'test', 'username': 'test'},
        {
            'invalid': ['email', 'password'],
            'message': 'Sign up data are invalid or non-unique.'
        }
    ),
    (
        {'email': 'test@example.com', 'password': 'test', 'username': 'test'},
        {
            'invalid': ['password'],
            'message': 'Sign up data are invalid or non-unique.'
        }
    ),
]


@pytest.mark.parametrize('data', test_data_422)
def test_sign_up_return_no_data(client, data):
    """
    Test if valid return code is returned
    when not enough data is supplied
    """
    response = client.post('/auth/signup', json=data)
    assert response.status_code != 200
    assert response.status_code == 422


@pytest.mark.parametrize('data,expected', test_data_400)
def test_sign_up_return_bad_request(client, data, expected):
    """
    Test if valid return code is returned
    when invalid data is supplied
    """
    response = client.post('/auth/signup', json=data)
    assert response.status_code != 200
    assert response.status_code == 400
    assert response.get_json() == expected


def test_sign_up_return_ok(client):
    """
    Test ok reposnse and check for duplicity
    """
    data = {'email': 'test@example.com',
            'password': 'P@ssword00', 'username': 'test'}
    response = client.post('/auth/signup', json=data)
    assert response.status_code == 200
    # test duplicate entry
    response = client.post('/auth/signup', json=data)
    assert response.status_code != 200
    assert response.status_code == 400
