def sum(n):
   if n == 1:
       return 0
   return n + sum(n-1)

a = sum(6)

print(a)
# n = 6
# 1) 6 + sum(5)  
# n = 5
# 2) 5 + sum(4)
# n = 4
# 3) 4 + sum(3)
#n = 3
# 4) 3 + sum(2)
# n = 2
# 5. 2 + sum(1)



# Which of the below are valid functions in Python? (Select all that apply)
some = ["aaa", "bbb"]

#1
def aa(some):
   return

#2
# def aa(some, 5):
#    return

#3
def aa():
   return

#4
def aa():
   return "aaa"


# If you modify the code above and change filter() function to map() function, what will be the list elements in the output that were not there earlier?
numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)