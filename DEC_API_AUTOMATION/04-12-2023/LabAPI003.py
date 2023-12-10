import requests

def main():
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1130")  # if you run this you won't get to see any results
    # response_body = requests.get("https://restful-booker.herokuapp.com/booking/718") # id is not exist, will gives you an assertion error
    assert response_body.status_code == 200 # if the status_code != 200 it will gives you an error


if __name__ == '__main__':
    main()


# def main():
#     id = "718"
#     url = "https://restful-booker.herokuapp.com/booking/"
#     full_url = url + id
#     print(full_url)
#     response_body = requests.get(full_url)
#     assert response_body.status_code == 200
#
#
# if __name__ == '__main__':
#     main()