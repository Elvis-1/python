"""
Indentation
Indentation is used to define code blocks in Python. Unlike many programming languages that use braces {} to group code, Python uses indentation.

Indentation is mandatory in Python and is used to indicate which statements belong to loops, functions, conditionals, and other structures.

if x > 0:  # Colon indicates the start of the block
    print("Positive")  # Indented 
else:
    print("Non-positive") # Indented


Comments
Single-line comments
Placing a  #  symbol in front of the text you want to be a comment causes Python to ignore everything from that point until the end of the current line.


# Single Line comment


Multi-line comments
Multi-line comments can be created using triple quotes (either single or double quotes). This is often used for documentation strings (docstrings) in functions, classes, and modules.

Inline/code comments
The  #  symbol will cause Python to ignore everything from that point until the end of the current line, so inline comments can be created in this way.

x = 1 # assigns value of 1 to x
Colon (:): Used to indicate the start of a code block, such as in loops, conditionals, and function definitions.

if x > 0:  # Colon starts the block
    print("Positive")

Built-in Functions
print()
This function looks for the default output device, your terminal, and displays the value passed to it.

print("Hello")

input()
This function looks for the default input device, your keyboard, and captures the value. This value can then be assigned or used.

print("Where do you live?")
location = input()
print("So you live in " + location)

Note: The code block above will create a prompt for the user asking "Where do you live?". The user will then enter the response and press the Return key to continue execution of the remaining code. The response entered by the user is stored, returned as an output, or can be assigned to some variable depending on the context of usage.

len()
This function returns the length or the count of the elements contained within the structure it is applied on. This may be a string, array, list, tuple, dictionary or any sequence.

len("Hello")
5

str()
This function can be used to convert the provided value into a String

str(55)
'55'

int()
This function can be used to convert the provided value into an int

int('75')
75

float()
This function can be used to convert the provided value into a float

some_int = 10
float(some_int)
10.0

Creating Functions
Functions in Python require a keyword to define them : def   followed by an identifier (a name) this forms the function signature. The body of the function contains the code to run when the function is called.


def say_hello():
    return "Hello there!"

# With parameters
def say_hello(you):
    return "Hello " +  you



"""