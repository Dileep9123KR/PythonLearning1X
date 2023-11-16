# iteration

my_dict = {'c': 5, 'a': 1, 'b': 3, 'e': 7}
for k,v in my_dict.items():
    print(k,v)

for k,v in my_dict.items():
    if k == 'c':
        print("Key -c- is found")

out = 'b' in my_dict
print(out)
