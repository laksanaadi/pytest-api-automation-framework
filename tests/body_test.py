import requests

BASE_URL = "https://restful-booker.herokuapp.com/"

def test_create_booking():
    url = f"{BASE_URL}/booking"

    payload = {
        "firstname": "Adi",
        "lastname": "QA",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2026-02-22",
            "checkout": "2026-02-24"
        },
        "additionalneeds": "Dinner"
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert "bookingid" in response.json()