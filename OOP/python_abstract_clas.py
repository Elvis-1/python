from abc import ABC, abstractmethod
#In object oriented programming, the abstract class is a type of class for which you cannot create an instance

#  Implementation in abstract classes can be done in two ways. One is that, as base abstract classes lack implementation of their own, the methods must be implemented by the derived class


# The module is known as the abstract base class or ABC, and needs to be imported with some code. After that, you can create a class called SomeAbstractClass and pass in the ABC module so that it inherits that class. The next step is to import the abstract method decorator inside the same module.

# A decorator is a function that takes another function as its arguments and gives a new function as its output. 


# Finally, here you'll define an abstractmethod which cannot be called on an object of this class.

# You will be able to call this method over objects of classes that inherit from this class. 


# Similarly, we can define abstract methods with the help of what we call an abstract method decorator present inside the same module

class Employee(ABC):
    @abstractmethod
    def donate(self):
        pass

class Donation(Employee):
    def donate(self):
        a = input('How much would you like to donate? ')
        return a
    
amounts = []
john = Donation()
j = john.donate()
amounts.append(j)

peter = Donation()
p = peter.donate()
amounts.append(p)

print(amounts)


