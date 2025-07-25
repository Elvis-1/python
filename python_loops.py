favorites = ['Potatoes', 'Tomatoes', 'Bannana','Plantain'];

# range(start,stop,steps) stop value is non inclusive
for i in range(10):
    print('Looping ..',i)

for item in favorites:
    print('I like desert',item)

# in a standard for loop, you don't have access to the index, so we use the enumerate

for idx, item in enumerate(favorites):
    print(idx,item)


count = 0
while count < len(favorites):
    print("I like this desert", favorites[count])
    count = count+1


# Practicing control flow and loops

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        print('Yes one of my favorite desserts is', dessert) 
    else:
        print('No sorry, that dessert is not on my list')

# Break
# Use break statement to make the code work as expected when it gets to a dessert that is present in the favorites

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
    else:
        print('No sorry, not a dessert on my list')

# to avoid repitition
for dessert in favorites:
    if dessert == 'Pudding':
        print('Yes one of my favorite desserts is', dessert)
        break 
else:
        print('No sorry, not a dessert on my list')
    

# Continue
# Similar to break, continue can be used to control the iteration of the loop. The key difference is that it can allow you to skip over a section of the loop but then continue on with the rest. If you change your code to this, you will notice the outcome will print everything except the Churros dessert.

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        continue
    print('Other desserts I like are', dessert)

#     Pass
# The pass statement allows you to run through the loop in its entirety and effectively ignore that the if condition has been satisfied.

#Starter Code
favorites = ['Creme Brulee', 'Apple Pie', 'Churros', 'Tiramisú', 'Chocolate Cake']

for dessert in favorites:
    if dessert == 'Churros':
        pass
    print('Other desserts I like are ***', dessert) 
    