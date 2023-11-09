with open('sample.txt', 'r') as file:
    print(file.read())
    print(file.read(5)) # print only 5 characters
    print(file.readline()) # only one line
    print(file.readlines()) # list of lines