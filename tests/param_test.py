import requests

BASE_URL = "http://www.omdbapi.com/"

def test_get_movie_success():
    params = {
        "apikey": "cc99fc43",
        "t": "lord"
    }

    response = requests.get(BASE_URL, params=params)

    assert response.status_code == 200

    body = response.json()
    assert body["Title"] == "The Lord of the Rings: The Fellowship of the Ring"
    assert body["Response"] == "True"