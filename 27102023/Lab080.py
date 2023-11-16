# Merging of tuple

tuple3 = tuple(["Dileep","Dilu"])
print(tuple3)
print(tuple3[0])
print(tuple3[1])

hero_team1 = ("Batman", "Bruce Wayne")
hero_team2 = ("Spider Man", "Peter Parker")

awesome_team = hero_team1 + hero_team2
print(awesome_team)

# convert tuple to List
f_tuple = (10,12,14,16,18)
print(list(f_tuple))

# we can assign multiple values like below in tuple

a,b,c = (10,20,30)
print(a)
print(b)
print(c)

# search in Tuple

countries = ("India", "Korea", "Japan","Sweden")
print(countries)
print("Korea" in countries)
print("Sri Lanka" in countries)