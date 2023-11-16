# A pure function is a function that does not change or have any effect on a variable, data, list, or sets beyond its own scope
myList = [1,2,3,4]

# not a pure function 
def addToList(item):
    return myList.append(item)

# addToList(5)

#convert the function above to a pure function

def addToList2(list,item):
    nl = list.copy()
    nl.append(item)
    return nl

newList = addToList2(myList,5)
print(newList)
print(myList) # the original list remains thesame




