# Ordered Dictionary - key-value pairs based on the order of insertion

my_dict = {'c': 5, 'a': 1, 'b': 3, 'e': 7}
print(my_dict)


from collections import OrderedDict
od = OrderedDict()
od['c'] = 5
od['a'] = 1
od['b'] = 3
od['e'] = 9
od['d'] = 7

print(od)

keys = list(od.keys())
print(keys)
sort_keys = sorted(keys)
print(sort_keys)

od1 = OrderedDict()
od1[sort_keys[0]]= 1
od1[sort_keys[1]]= 3
od1[sort_keys[2]]= 5
od1[sort_keys[3]]= 7
od1[sort_keys[4]]= 9

print(od1)