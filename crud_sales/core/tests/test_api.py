from .fixtures import client, single_sale, expected_sale
import json

def test_get_sales_by_state(client, single_sale):
    response = client.get('/api/sales_by_state')
    expected_json = [
        {"state": "Pará", "total": float(100.99)}
    ]
    assert json.loads(response.content) == expected_json
    assert response.status_code == 200

def test_get_download_csv(client):
    response = client.get('/api/download_csv')
    assert response.status_code == 200

def test_get_sales(client, expected_sale):
    response = client.get('/api/sales')
    assert json.loads(response.content) == [expected_sale]
    assert response.status_code == 200

def test_get_sing_sale(client, db, expected_sale):
    response = client.get(f'/api/sales/123')
    assert json.loads(response.content) == expected_sale
    assert response.status_code == 200

def test_create_sale(db, client):
    response = client.post(f'/api/sales', data={
        "id": 1234564,
        "created_at": "2022-05-01T10:53:30.121Z",
        "total": 0,
        "status": "string",
        "products_count": 0,
        "state": "string"
        }, content_type='application/json')
    assert response.status_code == 200

def test_create_sale_must_return_message_if_already_exist(db, client):
    response = client.post(f'/api/sales', data={
        "id": 123,
        "created_at": "2022-05-01T10:53:30.121Z",
        "total": 0,
        "status": "string",
        "products_count": 0,
        "state": "string"
        }, content_type='application/json')
    assert response.json() == {"Failed": "Sale id already exists"}


def test_update_sale(client, db):
    payload = {
        "id": 5,
        "created_at": "2022-01-01T00:00:00Z",
        "total": 100.99,
        "status": "COMPRA",
        "products_count": 5,
        "state": "Pará",
    }
    response = client.put(f'/api/sales/123', data=payload, content_type='application/json')
    assert response.status_code == 200

def test_delete_sale(db, client):
    response = client.delete('/api/sales/123')
    assert response.status_code == 200

def test_return_404_if_sale_not_exist(client):    
    response = client.get('/api/sales/1234')
    assert response.status_code == 404