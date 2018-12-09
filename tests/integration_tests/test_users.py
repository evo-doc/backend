import pytest
from tests.test_helpers import get_token
from evodoc.models import User

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

test_patch_user_error = [
    (
        {},
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        },
    ),
    (
        {
            'email': 'notanemail'
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'invalid': ['email'],
            'message': 'Supplied email is not valid.'
        },
    ),
    (
        {
            'username': 'testuser2'
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'invalid': ['username'],
            'message': 'This username is already in use.'
        },
    ),
    (
        {
            'email': 'test2@login.com'
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'invalid': ['email'],
            'message': 'This email is already in use.'
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


@pytest.mark.parametrize('data, login, expected', test_patch_user_error)
def test_patch_user_error(client, data, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.patch('/users/account', json=data, headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_patch_user_ok(client, db):
    testuser = User("testuserx", "testuserx@test.com", "Test@1010")
    db.session.add(testuser)
    db.session.commit()

    token = get_token(client, {
        'login': 'testuserx',
        'password': 'Test@1010'
    })
    headers = {'Authorization': 'Bearer ' + token}
    data = {
        'email': 'newtest@test.com',
        'name': 'John Doe',
        'username': 'xddddddd'
    }

    response = client.patch('/users/account', json=data, headers=headers)

    assert response.status_code == 200
    rdata = response.get_json()
    assert data['email'] == rdata['email']
    duser = db.session.query(User).getByEmail(data['email'])
    assert duser is not None
    assert duser.email == data['email']
    assert duser.fullname == data['name']
    assert duser.name == data['username']


def test_delete_user_ok(client, db):
    testuser = User("testusery", "testusery@test.com", "Test@1010")
    db.session.add(testuser)
    db.session.commit()

    token = get_token(client, {
        'login': 'testusery',
        'password': 'Test@1010'
    })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.delete('/users/account', headers=headers)

    assert response.status_code == 200
    duser = db.session.query(User).getByEmail('testusery@test.com')
    assert duser.delete is not None
