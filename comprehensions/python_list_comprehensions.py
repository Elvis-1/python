# Comprehensions in Python are a way to create a new sequence from an already existing sequence.

# There are four main types of comprehensions in Python: 

# List comprehension 

# Dictionary comprehension 

# Set comprehension 

# Generator comprehension


# -- List comprehension -- #

# The syntax for list comprehension is:

# [ <expression> for x in <sequence> if <condition>]

data = [2,3,4,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list

def updateTheGlobalList(data):
    data = [x+3 for x in data]
    return data

# data = updateTheGlobalList(data)
# print("Updating the list: ",data)
# print(data)

def creatingANewListWithUpdatedValues(data):
    new_data = [x*3 for x in data]
    return new_data
# print("Creating new list: ", creatingANewListWithUpdatedValues(data))
# print('Global list: ',data)

# Ex3: With an if-condition: Multiples of four:
def divisibleByFourWithIf(data):
    fourX = [x for x in data if x%4 == 0]
    return fourX

# print("Divisible by four", divisibleByFourWithIf(data))

def updatingTheListWithIf(data):
    data = [x-1 for x in data if x%4 == 0 ]
    return data

# print("Divisible by four minus one: ", updatingTheListWithIf(data))

def gettingMultiplesOfNineWithRange():
    nines = [x for x in range(100) if x%9 == 0]
    return nines
# print(gettingMultiplesOfNineWithRange())

def updateListWithForLoop(data):
    for x in range(len(data)):
     data[x] = data[x] + 3
    return data

data = updateListWithForLoop(data)
print(data)    


