import pytest
from tests.test_helpers import get_token


def createProject(client):
    projectToken = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010'
    })
    projectHeaders = {'Authorization': 'Bearer ' + projectToken}
    projectData = {
        'name': 'Test project',
        'description': '',
        'collaborators':  {
            'contributors': [
                'testuser3'
            ]
        }
    }
    projectResponse = client.post(
        '/projects/project', json=projectData, headers=projectHeaders)
    assert 2 == projectResponse.get_json()['id']
    projectResponse = client.post(
        '/projects/project', json=projectData, headers=projectHeaders)
    assert 3 == projectResponse.get_json()['id']
    projectResponse = client.post(
        '/projects/project', json=projectData, headers=projectHeaders)
    assert 4 == projectResponse.get_json()['id']


test_create_module_error = [
    (
        {
            "project": 4000,
            "name": "nechci pridavat constrainty",
            "description": "kek",
            "dependency": "independent",
            "content": {
                "type": "markdown",
                "body": "",
            },
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 404,
            'message': 'Project not found.',
            'invalid': [
                'project',
            ],
        }

    ),
    (
        {
            "project": 3,
            "name": "--",
            "description": "kek",
            "dependency": "independent",
            "content": {
                "type": "markdown",
                "body": "",
            },
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'name',
            ],
        }

    ),
    (
        {
            "project": 3,
            "name": "a",
            "description": "kek",
            "dependency": "independent",
            "content": {
                "type": "markdown",
                "body": "",
            },
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'name',
            ],
        }

    ),
    (
        {
            "project": 3,
            "name": "aaaa",
            "description": "kek",
            "dependency": "independent",
            "content": {
                "type": "markdown",
                "body": "",
            },
        },
        {
            'login': 'test2@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 403,
            'message': 'Access denied (no rights)',
            'invalid': [
                'project',
            ],
        }

    ),
    (
        {
            "project": 3,
            "name": "aaaa",
            "description": "kek",
            "dependency": "independent",
            "content": {
                "type": "markdown",
            },
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'content',
            ],
        }

    ),
    (
        {
            "project": 3,
            "name": "aaaa",
            "description": "kek",
            "dependency": "independent",
            "content": {},
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 422,
            'message': 'Not enough data to process the request.',
            'invalid': [
                'content',
            ],
        }

    ),
    (
        {
            "project": 3,
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 422,
            'message': 'Not enough data to process the request.',
            'invalid': [
                'name',
                'description',
                'content',
                'dependency',
            ],
        }

    ),
    (
        {
            "project": 4,
            "name": "k k_KEK",
            "description": "",
            "dependency": [
                "--",
            ],
            "content": {
                "type": "text",
                "body": "reeeeeeeeeeeeeeeeee",
            },
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'dependency',
            ],
        }

    ),
    (
        {
            "project": 3,
            "name": "k k_KEK",
            "description": "",
            "dependency": [
                "----------",
            ],
            "content": {
                "type": "text",
                "body": "reeeeeeeeeeeeeeeeee",
            },
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'dependency',
            ],
        }

    ),
]


test_view_module_error = [
    (
        10,
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 404,
            'message': 'Module not found.',
        }

    ),
    (
        1,
        {
            'login': 'test2@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 403,
            'message': 'Access denied (no rights)',
        }

    ),
]


test_patch_module_error = [
    (
        100,
        {
            "name": "aa",
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 404,
            'message': 'Module not found.',
            'invalid': [
                'module',
            ],
        }

    ),
    (
        1,
        {
            "name": "a",
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'name',
            ],
        }

    ),
    (
        2,
        {
            "name": "--",
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'name',
            ],
        }

    ),
    (
        1,
        {
            "name": "aaaa",
        },
        {
            'login': 'test2@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 403,
            'message': 'Access denied (no rights)',
            'invalid': [
                'project',
            ],
        }

    ),
    (
        1,
        {
            "content": {
                "type": "markdown",
            },
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'content',
            ],
        }

    ),
    (
        1,
        {
            "content": {},
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'content',
            ],
        }

    ),
    (
        1,
        {
            "dependency": [
                "---",
            ],
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'dependency',
            ],
        }

    ),
    (
        1,
        {
            "dependency": [
                "-----",
            ],
        },
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 400,
            'message': 'Module data are invalid or non-unique.',
            'invalid': [
                'dependency',
            ],
        }

    ),
]


test_delete_module_error = [
    (
        100,
        {
            'login': 'test@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 404,
            'message': 'Module not found.',
            'invalid': [
                'module',
            ],
        }

    ),
    (
        2,
        {
            'login': 'test2@login.com',
            'password': 'Test@1010',
        },
        {
            'code': 403,
            'message': 'Access denied (no rights)',
            'invalid': [
                'project',
            ],
        }

    ),
    # (
    #     1,
    #     {
    #         'login': 'test@login.com',
    #         'password': 'Test@1010',
    #     },
    #     {
    #         'code': 400,
    #         'message': 'Module can not be deleted.',
    #         'invalid': [
    #             'dependency',
    #         ],
    #     }

    # ),
]

# @pytest.mark.dependency(depends=['test_create_project_ok'])


def test_create_module_ok(client):
    createProject(client)
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010',
    })
    headers = {'Authorization': 'Bearer ' + token}
    data = {
        "project": 3,
        "name": "--",
        "description": "",
        "dependency": "independent",
        "content": {
            "body": "reeeeeeeeeeeeeeeeee",
        },
    }
    response = client.post('/modules/module', json=data, headers=headers)

    assert response.get_json()['id'] == 1
    assert response.status_code == 200
    assert response.get_json()['name'] == '--'

    token = get_token(client, {
        'login': 'test3@login.com',
        'password': 'Test@1010',
    })
    headers = {'Authorization': 'Bearer ' + token}
    data = {
        "project": 3,
        "name": "k k k_KEK",
        "description": "",
        "dependency": [
            "--",
        ],
        "content": {
            "type": "text",
            "body": "reeeeeeeeeeeeeeeeee",
        },
    }
    response = client.post('/modules/module', json=data, headers=headers)

    assert response.status_code == 200
    assert response.get_json()['name'] == 'k k k_KEK'

    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010',
    })
    headers = {'Authorization': 'Bearer ' + token}
    data = {
        "project": 4,
        "name": "---",
        "description": "",
        "dependency": "independent",
        "content": {
            "body": "reeeeeeeeeeeeeeeeee",
        },
    }
    response = client.post('/modules/module', json=data, headers=headers)

    assert response.status_code == 200
    assert response.get_json()['name'] == '---'


@pytest.mark.parametrize('data,login,expected', test_create_module_error)
def test_create_errors(client, data, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.post('/modules/module', json=data, headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    for each in response.get_json()['invalid']:
        assert each in expected['invalid']


@pytest.mark.parametrize('id,login,expected', test_view_module_error)
def test_view_error(client, id, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/modules/' + str(id), headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']


def test_view_ok(client):
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010',
    })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.get('modules/2', headers=headers)

    assert response.status_code == 200
    assert response.get_json()['project_id'] == 3
    assert response.get_json()['name'] == 'k k k_KEK'
    assert response.get_json()['description'] == ''
    assert response.get_json()['dependency'] == [
        '--',
    ]

    assert eval(response.get_json()['content'])['type'] == "text"
    assert eval(response.get_json()['content'])[
        'body'] == "reeeeeeeeeeeeeeeeee"


@pytest.mark.parametrize('id, data,login,expected', test_patch_module_error)
def test_patch_errors(client, id, data, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.patch('/modules/' + str(id), json=data, headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_patch_ok(client):
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010',
    })
    headers = {'Authorization': 'Bearer ' + token}
    data = {
        "description": "kkk",
    }
    response = client.patch('/modules/1', json=data, headers=headers)

    assert response.status_code == 200
    assert response.get_json()['name'] == '--'
    assert response.get_json()['description'] == 'kkk'


@pytest.mark.parametrize('id, login, expected', test_delete_module_error)
def test_delete_error(client, id, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.delete('/modules/' + str(id), headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_delete_ok(client):
    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010',
    })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.delete('modules/2', headers=headers)

    # assert response.status_code == 200
    # assert response.get_json()['invalid'] == "Module was deleted."
    assert response.get_json()['message'] == 'Module was deleted.'

    response = client.delete('modules/1', headers=headers)

    # assert response.status_code == 200
    # assert response.get_json()['invalid'] == "Module was deleted."
    assert response.get_json()['message'] == "Module was deleted."
