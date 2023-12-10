# There are three types of testing frameworks available in Python
# 1. Unit test 2. Nose 3. PyTest
# Every test case will starts from test_name.py : we are learning about Pytest

# How to do Create Booking by using PyTest - and make an allure report in the end
# Create a booking (POST method)
# URL
# HEADERs
# BODY(PAYLOAD) - JSON
# TOKEN
# Verify the Booking ID, Booking information as JSON

import requests
import pytest


@pytest.mark.positive
def test_create_booking_positive_tc():
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
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "Sarah", "Incorrect Firstname"


@pytest.mark.negative
def test_create_booking_negative_tc():
    print("Create booking testCase")
    URL = "https://restful-booker.herokuapp.com/booking"
    headers = {"Content-Type": "application/json"}
    json_payload = {}
    response = requests.post(url=URL, headers=headers, json=json_payload)

    # Assertion
    assert response.status_code == 500
    # Get the response body and verify the JSON, BookingID is not none
    data = response.json()
    assert data["bookingid"] is not None
    assert data["booking"]["firstname"] == "John", "Incorrect Firstname"