# Task
# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird



# n = input("What is n?: ")
# n = int(n)
# if n % 2:
#     print('Weird')
# if n % 2 == 0:
#     if(n >= 2 and n <=5):
#         print("Not Weird")
#     if(n >= 6 and n <=20):
#         print("Weird")
#     if(n > 20):
#         print("Not Weird")


# Arithmetic Operators

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

a = 5
b = 2
# print(a + b)
# print(a - b)
# print(a * b)

def is_leap(year):
    leap = False
    
    # Write your logic here

     # if a reminder is returned, it means its true therefore, leap is false
    if year % 4 == 0:
      leap = True
      if year % 100 == 0:
          leap = False
          if  year %  400 == 0:
            leap = True

    return leap

# Print the list of integers from  through  as a string, without spaces.
def getInput():
 n = int(input("Insert your number: "))
 if(n == 0):
   print(str(n))
   pass
 for i in range(1,n+1,1):
   print(i,end=",")

# You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following: Hello firstname lastname! You just delved into python

# Complete the 'print_full_name' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING first
#  2. STRING last

def print_full_name(first, last):
    # Write your code here
    print('Hello '+ first +' '+ last +'!'+ ' You just delved into python')
print_full_name('Elvis','Igiebor')



# Task

# Now, let's use our knowledge of sets and help Mickey.

# Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.


# form = sum of distincts heights / total numb of distinct heights

def average(array):
    # your code goes here
    s=set(array)
    a=0
    for i in s:
        a=a+i
    print('first is '+ str(a))
    a/len(s)

def findAverage(array):
  #  sum(), len
  sumOfDistinctHeights = sum(array)
  totalNumberOfDistinctHeight = len(array)
  print('second ----')
  print(sumOfDistinctHeights)
  round(sumOfDistinctHeights / totalNumberOfDistinctHeight,3)


def findAve(array):
    # convert to distinct values
    dist = set(array)
    sum = 0
    for x in dist:
        sum = sum + x
    ave = sum/len(dist)
    return ave

a = input()
# split the inputl
list = a.split(),
# convert to integers
newList = list(map(int,list))
print(newList)
#https://www.hackerrank.com/challenges/symmetric-difference/problem?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=7-day-campaign


  


array = set([161, 182, 161, 154, 176, 170, 167, 171, 170, 174])
print(array)
#result = findAverage(array)

#findAve(array);  
#formatted_result = "{:.3f}".format(result)

# average(array)