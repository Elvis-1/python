for x in range(1, 4):
    pass
    # print(int((str((float(x))))))


sample_dict = {1: 'Coffee', 2: 'Tea', 3: 'Juice'}
for x in sample_dict:
    print(x)

def recursion(num):
    print(num)
    next = num - 3
    if next > 1:
        recursion(next)

recursion(11)
# 11, 8, 5, 2,

# Question 7
# What will be the type of time complexity for the following piece of code:

str = 'Pomodoro'
for l in str:
 if l == 'o':
    # str = str.split()
    print(str, end=", ")

def d():
    color = "green"
    def e():
        nonlocal color
        color = "yellow"
    e()
    print("Color: " + color)
    color = "red"
color = "blue"
d()

num = 9
class Car:
    num = 5
    bathrooms = 2

def cost_evaluation(num):
    num = 10
    return num

class Bike():
    num = 11

cost_evaluation(num)
car = Car()
bike = Bike()
car.num = 7
Car.num = 2
print(num)



class A:
   def a(self):
       return "Function inside A"

class B:
   def a(self):
       return "Function inside B"

class C:
   pass

class D(C, A, B):
   pass

d = D()
print(d.a())


