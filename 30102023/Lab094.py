# to list every options available with dictionary
print(dir(dict))

my_dict = {'a': 2, 'b': 5, 'c': 5, 'a':8}
print(my_dict)

copy_my_dict = my_dict.copy()
print(copy_my_dict)
clr_my_dict = my_dict.clear()
print(clr_my_dict)

print(copy_my_dict.items())
set_dict = set(copy_my_dict.items())
# print(set_dict[0])
print(set_dict)

knights = {'gallard': 'The pure', "Robin": 'the brave'}
print(knights)

for k,v in knights.items():
    print(k,v)