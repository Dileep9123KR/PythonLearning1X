# To make an API request we need Request Lid

import requests


# to make CRUD operations to perform (GET, POST, PUT, PATCH, DELETE and Verify)
# and also for using different HTTP methods

def main():
    # print("Hello")
    # to make a GET request - URL
    # response_body = requests.get("https://restful-booker.herokuapp.com/booking/718") id is not found 404
    response_body = requests.get("https://restful-booker.herokuapp.com/booking/1130")
    # print(response_body.text)
    # print(response_body.status_code)
    # print(response_body.json())
    if response_body.status_code == 200:
        print("TC#1 - GET request is Successful")
    else:
        print("TC#1 - GET request is not Successful")


if __name__ == "__main__":
    main()


# to make an API req.
# POST - url, Auth, headers, cookies, responseTime, JSON, file

# Validate in API testing
# response, headers, statuscode, responseTime, JSON Schema Validation
