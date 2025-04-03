from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_get_offers():
    response = client.get("/offers")
    assert response.status_code == 200
    assert response.json() == [
        {
            'id': 1,
            'location': 'Томск, пер. Лесной 10',
            'photos': ['url1', 'url2'],
            'price': 100,
            'rooms': 3
        },
        {
            'id': 2,
            'location': 'Томск, пер. Лесной 11',
            'photos': ['url3'],
            'price': 2000,
            'rooms': 3,
        },
    ]


def test_get_offer():
    response = client.get("/offers/1")
    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'location': 'Томск, пер. Лесной 10',
        'phone': '+7777777777',
        'photos': ['url1', 'url2'],
        'price': 100,
        'rooms': 3,
        'total_area': 200
    }