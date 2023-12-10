# for assertion we use "assert" now, for proper methods we need to use "PyTest"
# for that file name should start with "test_"
# here we don't need to create a main function

import pytest
import requests


def test_sample():
    assert 4 == 4


def test_sample2():
    assert 6 == 5


def test_get_request():
    id = "1044"
    url = "https://restful-booker.herokuapp.com/booking/"
    full_url = url + id
    print(full_url)
    response_body = requests.get(full_url)
    assert response_body.status_code == 200

    data = response_body.json()
    # Assertion starts here
    # Verifications of KEYS
    assert 'firstname' in data, "Firstname key is present"
    assert 'lastname' in data, "Lastname key is present"

    # Verifications of DATA
    assert data["firstname"] == "Sarah", "Incorrect Firstname"
    assert data["lastname"] == "Brown", "Incorrect Lastname"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Message"
