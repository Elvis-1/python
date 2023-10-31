# we use args when we are not sure of the number of arguments we are expectiong

def sum_of(*args):
    sum = 0
    for x in args:
        sum+=x
    return sum

print(sum_of(1,2,3,4))