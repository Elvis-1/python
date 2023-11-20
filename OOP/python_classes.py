class MyClass:
    a = 5
    print("Hello")

    def hello(self):
        print("Hello World")

myc = MyClass()
#print(MyClass.a)
print(myc.a)
print(myc.hello())

class House:
    '''
    This is a stub for a class representing a house that can be used to create objects and evaluate different metrics that we may require in constructing it.
    '''
    num_rooms = 5
    bathrooms = 2
    def cost_evaluation(self, rate):
        # Functionality to calculate the costs from the area of the house
        cost = rate * self.num_rooms
        return cost

house = House()
# print(house.num_rooms)
# print(House.num_rooms)

# You have created an instance of a class called house and then modified the attribute for that instance with a value of 7. It updates the value of the instance attribute, but not the class attribute.

house.num_rooms = 7 # this will only update the value of the instance attribute but not the class attribute

print(house.num_rooms)
print(House.num_rooms)


# This time, instead of an instance attribute, you will modify the class attribute by directly calling it over the class as follows:

House.num_rooms = 7
print(house.num_rooms)
print(House.num_rooms)

# You will notice that the changes on a class attribute will affect even the instances that you will create over it

#  Also note the use of the keywork self  in this example. self is a convention in Python, and you may use any other word in its place, but as a practice, it is easy to recognize

# It should be noted how any number of parameters can be passed to these instance methods but the first one is always the reference to the instance of that class.

