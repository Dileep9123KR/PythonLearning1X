import requests
import pytest

# def test_create_token():
#     url = "https://restful-booker.herokuapp.com/auth"
#     headers = {"Content-Type": "application/json"}
#     json_payload = {
#     "username" : "admin",
#     "password" : "password123"
#     }
#     response = requests.post(url=url, headers=headers, json=json_payload)
#     data = response.json()
#     print(data["token"])


def create_token():
    url = "https://restful-booker.herokuapp.com/auth"
    headers = {"Content-Type": "application/json"}
    json_payload = {
    "username" : "admin",
    "password" : "password123"
    }
    response = requests.post(url=url, headers=headers, json=json_payload)
    data = response.json()
    token = data["token"]
    print(token)
    return token



def create_booking():
    print("Create booking testCase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "firstname": "Sarah",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Assertion
    assert response.status_code == 200
    # Get the response body and verify the JSON, BookingID is not none
    data = response.json()
    booking_id = data["bookingid"]
    return booking_id


def test_put_request():
    # need bookingID and Token
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    put_url = URL + str(booking_id)
    cookie_value = "token="+create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie" : cookie_value
    }
    print(headers)

    json_payload = {
        "firstname": "Sarah",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response = requests.put(url=put_url, headers=headers, json=json_payload)

    # Assertion
    assert response.status_code == 200
    # Get the response body and verify the JSON, BookingID is not none
    data = response.json()
    # assert data["bookingid"] is not None
    assert data["firstname"] == "Sarah", "Incorrect Firstname"

def test_delete():
    URL = "https://restful-booker.herokuapp.com/booking/"
    booking_id = create_booking()
    put_url = URL + str(booking_id)
    cookie_value = "token=" + create_token()
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    print(headers)


    response = requests.delete(url=put_url, headers=headers)

    # Assertion
    assert response.status_code == 201
