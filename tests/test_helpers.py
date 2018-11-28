import re


def get_token(client, data):
    response = client.post('/auth/signin', json=data)
    assert response.status_code == 200
    assert re.match(r'[0-9a-fy\-]{36}',
                    response.get_json()['token']) is not None

    return response.get_json()['token']