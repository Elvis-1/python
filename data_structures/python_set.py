set_a = {1,2,3,4,5}

 # set can't have a repeated or duplicate value
 # unlike list, it is unordered

set_a.add(5) # it won't be added
set_a.remove(2)
set_a.discard(2)

set_b = {5,6,7,8}

# print(set_a[2]) # error

print(set_a.union(set_b))
print(set_a | set_b)

print(set_a.intersection(set_b))
print(set_a & set_b)

print(set_a.difference(set_b))
# print(set_a - set_b)

print(set_a.symmetric_difference(set_b))
# print(set_a ^ set_b)

for a in set_a:
     print(a)
     if( a == 3 in set_a):
       print(str(a) + ' is in set a')

platform = set('Hackerrank')
print(platform) # not ordered





