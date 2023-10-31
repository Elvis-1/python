list1 = [1,2,3,4,5]

list2 = ["A","B", "C"]

list3 = ["Hello", 1, True, 40.04]

# print the values
print(*list1)

print(list1, sep=" ")

# adding items to a list

list1.insert(len(list1), 6)
print(list1, sep=" ")
list1.append(7)
print(list1, sep=" ")
list1.extend([8,9,1,0])
print(list1, sep=" ")

# remove from a list
list1.pop(4)  #removes item at position 4
del list1[2]

#iterate through a list
for x in list2:
    print('value', x)

