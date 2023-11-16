# # str[start:stop:step] // slice function

# def reverseString(str):
#  reversedString = str[::-1]
#  return reversedString

# # re = reverseString('Elvis')
# print(reverseString('Elvis'))


# REVERSING A STRING WITH RECURSION AND SLICE IN PYTHON #

def reverseString(str):
    if(len(str) == 0):
        return str
    else:
        return reverseString(str[1:]) + str[0]
    
print(reverseString('Elvis'))

