# Functions in Python require a keyword to define them : def   followed by an identifier (a name) this forms the function signature. The body of the function contains the code to run when the function is called.

def say_hello():
    return "Hello there!"
print(say_hello())

# with parameters
def say_hello(you):
    return "Hello "+you
print(say_hello())