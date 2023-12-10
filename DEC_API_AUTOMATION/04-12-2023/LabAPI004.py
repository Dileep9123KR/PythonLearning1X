import requests


def main():
    id = "718"
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
    assert data["firstname"] == "John", "Incorrect Firstname"
    assert data["lastname"] == "Smith", "Incorrect Lastname"
    assert data["bookingdates"]["checkin"] == "2018-01-01", "Incorrect Message"

if __name__ == '__main__':
    main()