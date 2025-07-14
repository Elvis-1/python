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

count = 0
while count < len(favorites):
    print('I like ',favorites[count])
    count +=1








