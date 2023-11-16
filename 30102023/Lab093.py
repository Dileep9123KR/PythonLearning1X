phone_book = {"Adam": 98798745, "Ben": 78978956, "Christofer": 87987964, "Daniel": 878974785}
print(phone_book)
print(len(phone_book))

print(phone_book["Ben"])
print(phone_book["Daniel"])

# another method to get dict, using dict() function

phone_book2 = dict(Jerald=45612, Steven=68754, Amber=874568)
print(phone_book2)
print(phone_book2['Steven'])
print(phone_book2.get('Amber'))


personal_details = dict(name="Dileep", Age=32, isMale=True, Address="KL")
print(personal_details)
print(personal_details["name"])
print(personal_details.get('name'))
print(personal_details.values())

# if you have a duplicate key in the dict, the latest value will be used
my_dict = {'a': 2, 'b': 5, 'c': 5, 'a':8}
print(my_dict)

key = my_dict.keys()
values = my_dict.values()
print(key)  # output will be in list
print(values)  # output will be in list

keys_list = list(key)  # converting it to list from dict
print(keys_list[0])
print(keys_list[1])
print(keys_list[2])
