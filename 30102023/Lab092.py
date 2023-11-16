# Dictionary - An unordered collection of data in a key-value pair format, (Key and value pair) {}
# Keys should be string
# it allows duplicates
# it is very close to the JSON
# to access its elements , index is not possible, you need to use the key in the dict ro access the element

name = "Dileep"  # here key is name and it's value is "Dileep"

my_dict1 = {}
my_dict2 = dict()  # dictionary function

print(type(my_dict1))
print(type(my_dict2))

# samples

fDict = {"name": "Dileep", "Age": 32, "Addr": "Kerala"}
print(fDict)

sDict = dict(name="Dileep", Age=32, Addr="Kerala")
print(sDict)