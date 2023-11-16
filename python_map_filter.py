menu = ['espresso','macha', 'coffee','cake','soup','curtado', 'americano']

def find_coffee(coffee):
    if(coffee[0] == 'c'):
        return coffee

map_coffee = map(find_coffee,menu) # returns a new list of all the variables
print(map_coffee)

for x in map_coffee:
    print(x)

filter_coffee = filter(find_coffee,menu) # returns a new list that contains only variable that meets the condtion
print(filter_coffee)

for x in filter_coffee:
    print(x)















