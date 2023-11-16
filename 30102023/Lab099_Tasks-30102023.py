# Program 1:
# Find the maximum and minimum elements in a tuple.

my_tuple = (15, 8, 25, 36, 42, 10)
print("The max num is : ", max(my_tuple))
print("The min num is : ", min(my_tuple))


# Program 2:
# Find the intersection and union of two sets.

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}
print("The intersection nums are : ", set1.intersection(set2))
print("The union nums are : ", set1.union(set2))


# Program 3:
# Remove duplicate elements from a list.

my_list = [1, 2, 2, 3, 4, 4, 5]
print("After removing duplicates : ", set(my_list))


# Program 4:
# Remove a key-value pair from the dictionary.

my_dict = {'name': "Logan", 'Hero Identity': "Wolverine", 'Age': 120, 'Flaws': "adamantium bullet",
           'Special Ability': "Quick heal"}
del my_dict['Age']
print(my_dict)


# Program 5:
# Convert to Dict JSON Response and Print and Booking Id AND checkin and Checkout Data

api_response = {"bookingid": 2384,"booking": {
            "firstname": "PRAMOD",
            "lastname": "Dutta",
            "totalprice": 432,
            "depositpaid": False,
            "bookingdates": {
            "checkin": "2022-01-01",
            "checkout": "2022-01-01"
            },
            "additionalneeds": "Lunch"
            }
            }

print(api_response.get('bookingid'))
print(api_response.get('booking').get('bookingdates').get('checkin'))
print(api_response.get('booking').get('bookingdates').get('checkout'))
