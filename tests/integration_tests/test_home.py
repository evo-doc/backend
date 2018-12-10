from evodoc.models.user import User
from evodoc.models.project import Project
from evodoc.models.package import Package
from tests.test_helpers import get_token
import pytest

test_get_stats_error = [
    (
        {},
        {
            'code': 401,
            'invalid': ['token'],
            'message': 'Unauthorised user (missing or outdated token)'
        }
    )
]


def test_gethome(client):
    """
    Basic test if our app even runs
    """
    response = client.get('/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data == "Hello there"


@pytest.mark.parametrize('login, expected', test_get_stats_error)
def test_stats_get_error(client, login, expected):
    headers = {}
    if login != {}:
        token = get_token(client, login)
        headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/stats/common', headers=headers)

    assert response.status_code == expected['code']
    assert response.get_json()['message'] == expected['message']
    assert response.get_json()['invalid'] == expected['invalid']


def test_stats_get_ok(client, db):
    users = User.query.get_all().count()
    packages = Package.query.get_all().count()
    projects = Project.query.get_all().count()

    token = get_token(client, {
        'login': 'test@login.com',
        'password': 'Test@1010'
    })
    headers = {'Authorization': 'Bearer ' + token}

    response = client.get('/stats/common', headers=headers)

    assert response.status_code == 200
    data = response.get_json()
    assert data['users'] == users
    assert data['packages'] == packages
    assert data['projects'] == projects
