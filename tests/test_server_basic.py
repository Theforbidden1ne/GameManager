import requests


def test_games_endpoint():
    r = requests.get('http://localhost:5000/games', timeout=5)
    assert r.status_code == 200
    assert isinstance(r.json(), list)
