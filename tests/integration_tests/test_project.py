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

test_view_project_error = [
    (
        0,
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        }
    ),
    (
        0,
        {
            'login': 'test@login.com',
            'password': 'Test@1010'
        },
        {
            'code': 404,
            'invalid': ['id'],
            'message': 'Project doesn\'t exist.'
        }
    )
]

test_patch_project_error = [
    (
        0,
        {},
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        }
    ),
    (
        0,
        {},
        {
            'login': 'test@login.com',
            'password': 'Test@1010'
        },
        {
            'code': 404,
            'invalid': ['id'],
            'message': 'Project doesn\'t exist.'
        }
    ),
    (
        1,
        {
            'name': 'T',
            'description': 'Haha'
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010'
        },
        {
            'code': 400,
            'invalid': ['name'],
            'message': 'Project name is too short.'
        }
    ),
    (
        1,
        {
            'name': 'My project now'
        },
        {
            'login': 'test2@login.com',
            'password': 'Test@1010'
        },
        {
            'code': 403,
            'invalid': [],
            'message': 'Access denied (no rights)'
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

    assert response.status_code == 200
    assert response.get_json()['name'] == 'Test project'


@pytest.mark.parametrize('id,login,expected', test_view_project_error)
def test_view_error(client, id, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/projects/' + str(id), headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_view_ok(client):
    token = get_token(client, {
            'login': 'test@login.com',
            'password': 'Test@1010'
        })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.get('projects/1', headers=headers)

    assert response.status_code == 200
    assert response.get_json()['name'] == 'Test project'


@pytest.mark.parametrize('id, data, login, expected', test_patch_project_error)
def test_patch_error(client, id, data, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.patch('/projects/' + str(id), json=data, headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_patch_no_data(client):
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010'
    })
    headers = {'Authorization': 'Bearer ' + token}
    data = {}

    response = client.patch('projects/1', json=data, headers=headers)

    assert response.status_code == 200
    assert response.get_json()['name'] == 'Test project'


def test_patch_ok(client):
    token = get_token(client, {
            'login': 'test@login.com',
            'password': 'Test@1010'
        })
    headers = {'Authorization': 'Bearer ' + token}
    data = {
        'name': 'My Project Now',
        'description': 'Random text'
    }

    response = client.patch('projects/1', json=data, headers=headers)

    assert response.status_code == 200
    assert response.get_json()['name'] != 'Test project'
    assert response.get_json()['name'] == 'My Project Now'
    assert response.get_json()['description'] == 'Random text'
