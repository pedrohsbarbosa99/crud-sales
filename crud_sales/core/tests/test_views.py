from .fixtures import client

def test_home_must_return_200(client):
    response = client.get('')
    assert response.status_code == 200