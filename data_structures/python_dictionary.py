my_d = {1:"Test", "Name":"Jame"}

#add a item
my_d[2] = 'Test 2'

#update a value
my_d[1] = "Test 1"

#no duplicate key
my_d[1] = "Jame" #it rewrites the previous

#del an item
del my_d[1]

#iterate through a dict
for x in my_d:
    print(x) # prints keys

for key, value in my_d.items():
    print(str(key) + " : " + value)

print(my_d[2])
print(my_d['Name'])
print(my_d)