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

    return numberDict
# usingOneInputList(number)

# Using two input lists

def usintTwoInputList(number,months):
 monthsDict = {key:value for (key, value) in zip(number, months)}
 print("Using two lists: ", monthsDict)
 return monthsDict

# monthsDict = usintTwoInputList(number,months)

def usingOneInputList(monthsDict):
 months_dict = {key:value for key, value in monthsDict.items()}
 print("Using one lists: ", months_dict)
# monthsDict = {'January': 1, 'February': 2, 'March': 3}
# usingOneInputList(monthsDict)
















