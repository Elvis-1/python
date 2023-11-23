class A:
   def __init__(self, c):
       print("---------Inside class A----------")
       self.c = c
   print("Print inside A.")

   def alpha(self):
       c = self.c + 1
       return c

print(dir(A))
print("Instantiating A..")
a = A(1)
print(a.alpha())

class B:
   def __init__(self, a):
       print("---------Inside class B----------")
       self.a = a

   print(a.alpha())
   d = 5
   print(d)
   print(a)

print("Instantiating B..")
b = B(a)
print(a)

# Step 2: Comment out lines #13, 14, 21, 24, 27 and 28. Run the code again. 

# The output is:

# Hello World!
# Print inside A.
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'alpha']
# Instantiating A..
# 5
# Instantiating B..

# Even if you have commented out the creation of instances for both classes A and B, the output still shows “Print inside A” and “Print inside B” and also the value of variable d, which is 5. How is that possible?

# It's because statements inside a class body get executed irrespective of the instance creation. You will also see how the print statement “Inside class A”, which is inside the constructor, is not executed because it's inside a function. 

# Step 3: Now remove the comment for lines 21 and 24. 



