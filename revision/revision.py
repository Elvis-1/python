x = 1 +   2\
+3
print(x)

# indentation

name = "Beaut"

if(name == "Beauty"):
    print(name)

def isName():
    if(name == "Beauty"):
        print(True)
    else:
        print(False)
isName()

# python variable = "Python Variable"

a,b,c = 3,2,5
print(a)
print(b)
print(c)

# assigning multiple variables
d = e = f = 9
print(d)
print(e)
print(f)

del d
#print(d)  # This will raise an error since d is deleted

# datatypes
c = "God is good" # string
print(type(c))
d = 3.14
print(type(d))
e = 42 # integer
print(type(e))
f = [2,4,1] # list
print(type(f))
g = (1,2,3) # tuple
print(type(g))
h = {1,2,3} # set
print(type(h))
i = {'name': 'Alice', 'age': 30} # dictionary
print(type(i))

# string
b = "This is a single line string"
print(b)
# multiline string
c = "This is a multiline"\
      " string, it is too long so we used back slash"
print(c)
# concatenation
print(b + " " + c)
# using string index
print(len(b))
print(b[22])
# using escape and new line characters 
print("Hello\nWorld")
print('Learning\nisn\'t always easy')
# using raw string
print(r'Hello isn\'t World')

# input and output
# name1 = input("What is your first name?")
# name2 = input("What is your second name?")

# print(name1 + ' ' + name2)

# using format in print
# name1 = input("What is your first name?")
# name2 = input("What is your second name?")

# print("{} {}".format(name1,name2))

# calculations

# firstNum = input("Pick a number")
# secondNum = input("Another number")

# sumOfNumber = int(firstNum) + int(secondNum)

# print("This is the sum of  the two numbers {}".format(sumOfNumber))


# control flows and conditionals

billTotal = 210

# discount1 = 10

if billTotal >= 100 and  billTotal < 200:
    print('Bill total is greater than or equal to 100')
elif billTotal > 200:
    print('Bill total is greater than 200')
else:
    print('Bill total is less than 100')


# looping constructs
name = 'Looping'
# for i in range(10):
#     print('Looping ...',i)

# for item in name:
#     print(item,end='')

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

# for index, item in enumerate(favorites):
#     print(index,item)

# for  item in favorites:
#     print(item)

# count = 0
# while count < len(favorites):
#     print('I like ',favorites[count])
#     count +=1


# Practicing control flow and loops
# In many cases, you may need to search for a particular item in a list

favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']
searchItem = 'Churros'
for item in favorites:
    if searchItem == item:
        print('I found my desert', item)
        break
else:
        print('My desert is not included!')

# for item in favorites:
#     if searchItem == item:
#         continue
#     print('These are other deserts', item)
   

for item in favorites:
    if searchItem == item:
        pass
    print('These are other deserts', item)


# NEXTED FOR LOOPS
# for time complexity, it is poor
#oute loop
for j in range(10):
    # inner loop
    for i in range(10):
        print(i, end=' ')
    print(' ')

# solve a control loop problems
num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# 1.   Under the num_list create a new for loop and print out each value on the list in sequential order.

for num in num_list:
    print(num, end=' ')

# 2.  Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition

for num in num_list:
    if num > 45:
        print(num)

# 3.  Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.

for num in num_list:
    if num > 45:
        print(num, 'Over 45')
    else:
        print(num, 'Under 45')

# 4.  Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number

for index, item in enumerate(num_list):
    if item == 36:
        print('Number found at position: ', index)

# 5.  Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
# 6.  Inside the for loop increment the counter by 1.
# 7.  Add a print statement outside the for loop to print the value of the count variable.
# 8.  Finally, add a break statement directly after the print statement inside the if condition for finding the number.

count = 0
for index, num in enumerate(num_list):
    count +=1
    if num == 36:
        print('Number found at position: ', index)
        break
 
print(count)


# python functions
def calculateTax(bill,taxRate):
    return (bill * taxRate)/100

print('Total tax is: ', calculateTax(100, 5))











