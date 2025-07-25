'''

Section 1: Introduction to Python
What are some real-life uses of Python? (Name at least 3.)

Why is Python considered a good language for beginners?

Section 2: Setting Up Python
What are some ways to check if Python is installed on your computer?

Name two different ways to run Python code.

Section 3: Python Syntax Basics
What is the purpose of comments in Python? How do you write them?

What are the four basic data types in Python?

How do you take user input in Python?

Section 4: Operators & Control Flow
What is the difference between == and = in Python?

What does the % operator do?

Write a Python statement that checks if a number is even using an if condition.

Section 5: Loops
What is the difference between a while loop and a for loop?

Write a for loop that prints numbers from 1 to 5.

Bonus Challenge
Write a Python program that:

Asks the user for their name.

If the name is longer than 5 letters, print: "That's a long name!"

Otherwise, print: "Nice name!"

'''
# Section 1: 

# it is used in web development, machine learning, data analytics and artificail intelligence
# it is considered a good language for beginners due to its simple syntax, it is close to the English language, and developers can write less and do more.


# Section 2: 
# run python --version or python3 --version
# while in the file, click on the play button in the right hand corner of vs code or write the file name in your terminal and press enter


# number 3
# comments are used for code documentation or for codes you don't want to run # single line comment. '''multiline comment'''
# Numeric, Sequence, boolean, dictionary, set;
# input()



# number 4
# == this is a logical operator, it checks for eqaulity. = is an assignment operators, it is used to assign values to a variable
# % it returns the reminder of a value

# number 5
value = 4
if value % 2 == 0:
    print(value, 'is an even value')
else:
    print(value, 'is not an even value')


for i in range(5):
    
    print(i+1)


yourName = input('What is your name:')
if(len(yourName) > 5):
    print("That's a long name!")
else:
    print("Nice name!")









