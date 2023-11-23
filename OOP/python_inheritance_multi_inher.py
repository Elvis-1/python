# Simple Inheritance

class A:
 pass

class B(A):
 pass

# If class A is the parent class and class B is inheriting from it, then class A is passed inside class B as a parameter. This will allow class B to directly access the attributes and methods inside class A.

# Multiple inheritance

# Example 1
class A:
   a = 1
   
class B:
   b = 2
   
class C(A, B):
   pass

c = C()
print(c.a, c.b)

# Multi-level inheritance

class A:
   a = 1

class B(A):
   a = 2

class C(B):
   pass

c = C()
print(c.a)


# The case above is an example of multi-level inheritance where the derived class C inherits from base class B. The class B is in turn a derived class of base class C. Class B here is an intermediary derived class. There are three levels of inheritance in this case, but it could be extended as long as I want, though it may become impractical after a while.


# Built-in functions

 # issubclass(class A, class B)

# Two classes are passed as arguments to this function and a Boolean result is returned. The above example can be extended as follows. 

print(issubclass(A,B))
print(issubclass(B,A))

class A:
	pass
class B(A):
	pass

b = B()
print(isinstance(b,B))
print(isinstance(b,B))

# super() function.

# The super() function is a built-in function that can be called inside the derived class and gives access to the methods and variables of the parent classes or sibling classes. Sibling classes are the classes that share the same parent class. When you call the super() function, you get an object that represents the parent class in return.

class Fruit():
    def __init__(self, fruit):
        print('Fruit type: ', fruit)


class FruitFlavour(Fruit):
    def __init__(self):
        super().__init__('Apple')
        print('Apple is sweet')

apple = FruitFlavour("")

