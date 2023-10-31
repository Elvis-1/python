# we use args when we are not sure of the number of arguments we are expectiong

def sum_of(**kwargs):
    sum = 0
    for x,v in kwargs.items():
        sum+=v
    return round(sum,2)

print(sum_of(coffee =2.99, cake=4.89, juice=2.99))