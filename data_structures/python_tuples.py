my_tuples = (1, "strings", 4.5, True)

print(my_tuples[1])

# count certain item
print(my_tuples.count('strings'))

print(my_tuples.index(4.5))

for x in my_tuples:
    print(x)

# the major difference between tuples and list is that tuples are immutable

my_tuples[3] = 5 # this will not work