# Instructions



num_list = [33,42,5,66,77,22,16,79,36,62,78,43,88,39,53,67,89,11]

# 1.   Under the num_list create a new for loop and print out each value on the list in sequential order.

for num in num_list:
       print(num, end=" ")
    

# 2.  Inside the for loop, create a condition that will look for all numbers that are greater than 45 and print out only numbers that meet that condition

for num in num_list:
    if num > 45:
       print("Over 45: ", num)
# 3.  Change the print statement to “Over 45” and add an else condition with a print statement of “Under 45”.
for num in num_list:
    if num > 45:
       print("Over 45: ", num)
    else:
        print("Under 45: ", num)
        
# 4.  Update the for loop to use the enumerate function so you can get and use the index. Alter the condition to look for number 36 and print out the following: ‘Number found at position: ‘, index number
for i, num in enumerate(num_list):
     if num_list[i] == 36:
      print("Number found at position ", i)
     

# 5.  Next, create a new variable called count and assign it a value of 0 and place it outside the for loop.
# 6.  Inside the for loop increment the counter by 1.
# 7.  Add a print statement outside the for loop to print the value of the count variable

count = 0
for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)

print(count)

# 8.  Finally, add a break statement directly after the print statement inside the if condition for finding the number.

count = 0

for x,num in enumerate(num_list):
    count += 1
    if num == 36:
        print('Number found at ', x)
        break

print(count)  

# a = isinstance(str, "aa")
# print(a)

if 1 in [3,4,5,6,7,1]:
    print("it is there")
else:
    print('its not there')

if 'bar' in {'foo':1, 'bar':2,'baz':3}:
    print(1)
    print(2)
    if 'a' in 'qux':
        print(3)
print(4)

a = 100
b = 50

# Write a Python if/else statement to assign the smaller of a and b to the variable m.
if a>b:
    m = b
    print(str(b) +' is smaller')
else:
    m = a
    print(str(a) + ' is smaller')

print("ab") if '123'.isdigit() else print("by")

x = 50
y = 40

if x < y:
    pass
else:
    pass


