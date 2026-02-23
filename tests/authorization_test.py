import requests

BASE_URL = "https://httpbin.org"

def test_basic_auth_success():
    url = f"{BASE_URL}/basic-auth/user/passwd"
    
    auth = ("user", "passwd")

    response = requests.get(url,auth=auth)

    assert response.status_code == 200

    body = response.json()
    assert body["authenticated"] is True
    assert body["user"] == "user"