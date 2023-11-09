import os
file_path = os.path.join(os.getcwd(), "test.txt")


#The open function is used for reading, writing and creating files.

# The open function accepts two arguments. The first is the file name and or the file location and the second argument is the mode

# It's also specifies if you want the file output in text or binary format.

# The close function is used for closing the open file connection, know that it does not take any arguments.

# There is one more way to open and close a file in Python and that's with open function. The advantage of using it is that it closes the file automatically


file = open(file_path, mode='r')

data = file.readline()

print(data)
file.close()

# using the 'with open' function

with open('test.txt', mode='r') as file:
    data = file.readline()
    print(data)

