import pytest
from tests.test_helpers import get_token


test_create_project_error = [
    (
        {},
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        }
    ),
    (
        {},
        {
            'login': 'test@login.com',
            'password': 'Test@1010'
        },
        {
            'code': 422,
            'invalid': [],
            'message': 'Not enough data to process the request.'
        }
    ),
]


@pytest.mark.parametrize('data,login,expected', test_create_project_error)
def test_create_errors(client, data, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.post('/projects/project', json=data, headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_create_ok(client):
    token = get_token(client, {
            'login': 'test@login.com',
            'password': 'Test@1010'
        })
    headers = {'Authorization': 'Bearer ' + token}
    data = {
        'name': 'Test project',
        'description': '',
        'collaborators':  {
            'contributors': []
            }
        }
    response = client.post('/projects/project', json=data, headers=headers)

    assert response.get_json()['message'] == ""
    assert response.status_code == 200
