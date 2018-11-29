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
