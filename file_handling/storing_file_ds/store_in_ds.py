import random

#Imagine you are trying to come up with a name for your new dog. You're really unsure of what you'd like to call the dog, so you decide to use your Python skills to help you decide

f = open('petnames.txt', 'r')
fCon = f.read()
#Get fCon variable into a list. The string "\n" is used to split the text where a new line is found.
fContent = fCon.split('\n')
print(fContent)
f.close()

# Now that I have all my potential pet names in a list, I can randomly pick a name from the f_content_list of names.

# I'll need to import the random module at the top of my code: import random.

# use the random module's choice() function: random.choice().

# The choice() function accepts a sequence parameter. A list is one of its accepted values. This means that I can now add another line of code at the very bottom of my program:

print(random.choice(fContent)) 

# Finally, If I had multiple files in my folder, I could allow myself to pick a file from which to read in a list of names.

f = input('What is your file name? ')

f_name = input('Type the file name: ')
f = open(f_name) # "r" omitted as it's the default
f_content = f.read()
f_content_list = f_content.split("\n")
f.close()
print(random.choice(f_content_list))