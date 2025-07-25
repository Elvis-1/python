#global scope
my_global = 10

def fn1():
    local_v = 5
    print('Access to global', my_global)

# print('Can\'t access local scope ', local_v)
# fn1()


def fn2():
    enclosed_v = 6
    def fn3():
        local_v = 4
        print("Access to Global variable ", my_global)
        print('Access to enclosed', enclosed_v)

    fn3()

fn2()

# Function and variable scope

# 1. Local scope
# Local scope refers to a variable that are declared inside a function. For example, in the code below, the variable total is only available to the code within the get_total() function. Anything outside of this function will not have access to it.

def get_total(a, b):
    total = a + b
    return total
print(get_total(5, 10))
#print('Can\'t access local scope ', total)  # This will raise an error because total is not defined in this scope


# 2. Enclosing scope
# Enclosing scope refers to a function inside another function or what is commonly called a nested function. 

# In the code below, I added a nested function called double_it to the get_total function. 

# As double_it() is inside the scope of the get_total() function, it can access the variable total declared in the enclosing function. However, the local variable double, defined inside double_it(), cannot be accessed from inside the get_total() function. The function double_it() is also called the inner function.

def get_total(a, b):
    total = a + b

    def double_it():
        double = total * 2
        print(double)
    double_it()
  #  print(double) # This will raise an error because double is not defined in this scope
    print(total)
get_total(5, 10)
#print('Can\'t access local scope ', double)  # This will raise an error because double is not defined in this scope


# 3. Global scope
# Global scope is when a variable is declared outside of a function. This means it can be accessed from anywhere. 

# In the code below, I added a global variable called special. This can then be accessed from both functions get_total() and double_it():

special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total
