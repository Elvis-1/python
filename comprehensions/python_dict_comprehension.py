# Dictionary comprehension takes one or two lists as input and creates a dictionary out of it

# dict = { key:value for key, value in <sequence> if <condition> }

# Using range() function and no input list

def usingRangeWithNoInputList():
    usingRange = {x:x*2 for x in range(12)}
    print("Using range(): ",usingRange)
# usingRangeWithNoInputList()

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list

def usingOneInputList(number):
    numberDict = {x:x**2 for x in number}
    print("Using one input list to create dict: ", numberDict)
# usingOneInputList(number)

# Using two input lists

def usintTwoInputList(number,months):
 months_dict = {key:value for (key, value) in zip(number, months)}
 print("Using two lists: ", months_dict)

# usintTwoInputList(number,months)


















