# List is mutable and it's content can be changed - [] square brackets

my_List = [1, 3, 5, 7, 9]
print(my_List)
my_List[2] = 11  # indexing values considering here 5 replaced by 11
print(my_List)
print(type(my_List))  # class List

# Tuple - it's immutable in nature, once you created a tuple it can't be changed - () normal brackets

cars = ("Mustang GT", "Carrera GT", "Supernova 305", "Lambo Gallard o")
print(cars)
print(type(cars))  # class tuple
#  cars [1] = "Bugatti XYD"  - tuple cannot change the data in it

car = ("Ford", False, 425, "Scorpio")  # Support different data types
print(car)

# contents can be duplicated in both List and Tuple
my_List = [1, 3, 5, 7, 9, 9]
print(my_List)

cars = ("Mustang GT", "Carrera GT", "Supernova 305", "Lambo Gallard o", "Lambo Gallard o")
print(cars)

# List can be converted to a tuple

my_List1 = [4, 6, 7, 8, 9]
print(my_List1)
print(tuple(my_List1))  # for converting list to Tuple we use a function known as tuple
