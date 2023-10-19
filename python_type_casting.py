
print(10 == 10)
# Python here perfoms what's known as "implicit type conversion"
print(10 == 10.00)

# when Python runs operations involving integers and floats, it implicitly converts the integers type to a float, and then completes the operation.
print(10 + 10.0)
print(type(10+10.0))

# everything that a user types in, is converted, by Python, to the string data type.
user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')
user_sum = user_num_1 + user_num_2
print(user_sum)

# In order to have my Python code work as I intended, I need to perform explicit type conversion.
user_num_1 = input('First number is: ')
user_num_2 = input('Second number is: ')
user_sum = float(user_num_1) + float(user_num_2)
print(user_sum)

#  it will throw the following error:
# num_1 = input('First number is: ')
# num_2 = input('Second number is: ')
# user_sum = float(num_1) + float(num_2)
# print("The sum of: " + num_1 + " and " + num_2 + " is " + user_sum)


# What this means is, I cannot concatenate a string and a float like that. In other words, although Python's implicit type conversion works when I use the + operator on strings and integers, it does not work on strings and floats.

# The solution to this is to perform explicit type conversion, as follows.

n1 = input('First number is: ')
n2 = input('Second number is: ')
user_sum = float(n1) + float(n2)
print("The sum of " + str(n1) + " and " + str(n2) + " is " + str(user_sum))

