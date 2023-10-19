# Spacing
#any ammount of whitespace on a single line is ok
x = 1  +   8
print(x)

# Incorrect
x = 1 
+2
print(x)

# correct
x = 1 \
+2
print(x)

# Indentation
name = "Elvis"
if (name == "Elvis"):
   print(name)

def say_hello():
    print("Hello there!")
print(say_hello())

def say_hello(): print("Hello there!")

print(say_hello())

# Incorrect

# def say_hello():
# print("Hello there!")

#     def say_hello():
# print("Hello there")

