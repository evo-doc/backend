from datetime import datetime, timedelta
from evodoc.models import UserToken
import pytest
import re


test_signup_data_422 = [
    {},
    {'email': ''},
    {'email': '', 'password': ''},
]

test_signup_data_400 = [
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

test_signin_data_422 = [
    {},
    {'login': ''},
    {'password': ''},
]

test_signin_data_400 = [
    (
        {'login': 'no-email', 'password': 'Nevim'},
        {
            'invalid': [],
            'message': 'Sign in data are invalid.'
        }
    )
]


@pytest.mark.parametrize('data', test_signup_data_422)
def test_sign_up_return_no_data(client, data):
    """
    Test if valid return code is returned
    when not enough data is supplied
    """
    response = client.post('/auth/signup', json=data)
    assert response.status_code != 200
    assert response.status_code == 422


@pytest.mark.parametrize('data,expected', test_signup_data_400)
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


@pytest.mark.parametrize('data', test_signin_data_422)
def test_sign_in_return_no_data(client, data):
    """
    Test if valid return code is returned
    when not enough data is supplied
    """
    response = client.post('/auth/signin', json=data)
    assert response.status_code != 200
    assert response.status_code == 422


@pytest.mark.parametrize('data,expected', test_signin_data_400)
def test_sign_in_return_bad_request(client, data, expected):
    """
    Test if valid return code is returned
    when invalid data is supplied
    """
    response = client.post('/auth/signin', json=data)
    assert response.status_code != 200
    assert response.status_code == 400
    assert response.get_json() == expected


def test_sign_in_return_ok(client):
    data = {'login': 'test@example.com',
            'password': 'P@ssword00'}

    response = client.post('/auth/signin', json=data)
    assert response.status_code == 200
    assert re.match(r'[0-9a-fy\-]{36}',
                    response.get_json()['token']) is not None


def test_authenticated_unauthorized(client):
    response = client.get('/auth/authenticated')

    assert response.status_code == 401


def test_authenticated_bad_token(client):
    response = client.get('/auth/authenticated',
                          headers={'Authorization': 'Bearer random-token'})

    assert response.status_code == 401


def test_authenticated_old_token(client, db):
    token = db.session.query(UserToken).first()
    token.update = datetime.now() - timedelta(hours=-1)
    db.session.commit()

    response = client.get('/auth/authenticated',
                          headers={'Authorization': 'Bearer ' + token.token})

    assert response.status_code == 200
    assert response.get_json() == {"message": "User is authenticated."}


def test_authenticated_ok(client):
    data = {'login': 'test@example.com',
            'password': 'P@ssword00'}

    response = client.post('/auth/signin', json=data)
    assert response.status_code == 200

    token = response.get_json()['token']
    assert re.match(r'[0-9a-fy\-]{36}', token) is not None

    response = client.get('/auth/authenticated',
                          headers={'Authorization': 'Bearer ' + token})

    assert response.status_code == 200
    assert response.get_json() == {"message": "User is authenticated."}


def test_logout_no_token(client):
    response = client.get('/auth/signout')

    assert response.status_code == 401


def test_logout_invalid_token(client):
    response = client.get('/auth/signout',
                          headers={'Authorization': 'Bearer random-token'})

    assert response.status_code == 401


def test_logout_ok(client):
    data = {'login': 'test@example.com',
            'password': 'P@ssword00'}

    response = client.post('/auth/signin', json=data)
    assert response.status_code == 200

    token = response.get_json()['token']
    assert re.match(r'[0-9a-fy\-]{36}', token) is not None

    response = client.get('/auth/signout',
                          headers={'Authorization': 'Bearer ' + token})

    assert response.status_code == 200

    response = client.get('/auth/authenticated',
                          headers={'Authorization': 'Bearer ' + token})

    assert response.status_code == 401
