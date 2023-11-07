# List

f_List = [1,2,3,4,5]
s_List = [1, True,"Name"]

print("Initial List :", f_List)

# Indexing

print("0 index element is", f_List[0])

# changing an element

f_List[1] = 20
print("List after changing the element :",f_List)

# append()

f_List.append(10)
print("List after appending :", f_List)

# extend()

f_List.extend([7,8])
print("List after extending :", f_List)

# insert()

f_List.insert(1, 'd')
print("list after inserting 'd' at index 1:", f_List)

# remove()

f_List.remove('d')
print("List after removing 'd':", f_List)

# clear() and copy()

f_List_copy = f_List.copy()
print("List after being copied: ",f_List_copy)

f_List_copy.clear()
print("List after cleared :", f_List_copy) # list becomes empty, not null

# index()

print("Index of 3 in the list :", f_List.index(3))
# print("Index of 3 in the list :", f_List_copy.index(3))  # will give you an error due to there is nothing in the list

f_List.sort()
print("List after sorting :",f_List)

# reverse()

f_List.reverse()
print("List after reversing :", f_List)
