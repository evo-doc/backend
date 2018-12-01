import pytest
from tests.test_helpers import get_token

test_get_users_error = [
    (
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        }
    )
]

test_get_user_error = [
    (
        'random',
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        }
    ),
    (
        'random',
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 404,
            'invalid': [],
            'message': 'Name not found.'
        },
    ),
]

test_get_our_data_error = [
    (
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        },
    ),
]


@pytest.mark.parametrize('login, expected', test_get_users_error)
def test_get_users_error(client, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/users', headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_get_users_ok(client):
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010'
    })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/users', headers=headers)

    assert response.status_code == 200


@pytest.mark.parametrize('name, login, expected', test_get_user_error)
def test_get_user_error(client, name, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/users/' + name + '/account', headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_get_user_ok(client):
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010'
    })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/users/testuser/account', headers=headers)

    assert response.status_code == 200


@pytest.mark.parametrize('login, expected', test_get_our_data_error)
def test_get_our_data_error(client, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/users/account', headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_get_our_data_ok(client):
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010'
    })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/users/account', headers=headers)

    assert response.status_code == 200
    data = response.get_json()
    assert 'name' in data
    assert 'email' in data
    assert 'avatar' in data
    assert 'fullname' in data