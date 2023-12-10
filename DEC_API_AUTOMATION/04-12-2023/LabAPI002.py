import requests

response_body = requests.get("https://restful-booker.herokuapp.com/booking/1130")
print(response_body.text)
print(response_body.headers)

# to verify the test cases we use assertion : to verify Expected Result with the Actual Result

