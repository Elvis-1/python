def divide_by(a,b):
    return a/b

try:
 ans = divide_by(40,5)
#  print(ans)
except:
    print("Something went wrong")


#----- handing generic exceptions ----#

def divide(a,b):
    return a/b

try:
 ans = divide_by(40,0)
 print(ans)

except Exception as e: # handling generic exception
  # print("Something went wrong", e)
  # print(e.__class__) #printing the particular exception class
  print('á')

# -- chaining exceptions --- #

def divide(a,b):
    return a/b

try:
 ans = divide(40,0)
 print(ans)

except ZeroDivisionError as d: # handling generic exception
   print(d, "You can not divide by zero")
   print(d.__class__) #printing the particular exception class

except Exception as e:
      print("Something went wrong", e)
      print(e.__class__)

#---- Exercise: Exceptions in Python ---#

# Your task in this exercise is to add code to trap exceptions and handle them in a more user-friendly way. 

#IndexError

# Starter code
def getItemInList(items):
 item = items[6]
 return item
try:
 item = getItemInList([1,2,3,4,5])
 print(item)
except IndexError as e:
  print(e,": Item does not exist in the list")


# FileNotFoundError

# The code below is looking for a file that does not exist. Add exception handling to catch this error and return the following "The file could not be found".

# Starter code

def openFile():
   with open('file_does_not_exist.txt', 'r') as file:
    print(file.read())

try:
   openFile()
except FileNotFoundError as f:
   print(f, 'The file could not be found')
   