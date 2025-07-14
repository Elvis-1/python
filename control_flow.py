

bill_total = 300

discount1 = 10
discount2 = 20

if bill_total > 100 and bill_total < 200:
    print("Bill is greater than 100")
    bill_total = bill_total - discount1

elif bill_total > 200:
    print("Bill is greater than 200")
    bill_total = bill_total - discount2
    print("Bill is greater than 200")
else:
    print("bill is less than 100")

print("Total bill: "+ str(bill_total))


# MATCH STATEMENT

http_status = 300

match http_status:
    case 200 | 201:
        print("Success")
    case 400:
        print('Bad Request')
    case 500 | 501:
        print("Server Error")
    case _:
        print("Default")

    
    # PYTHON'S TERNARY OPERATOR

    # <expr1> if <conditional_expr> else <expr2>

    # In the above example, <conditional_expr> is evaluated first. If it is true, the expression evaluates to <expr1>. If it is false, the expression evaluates to <expr2>.

raining = False 
print('Lets go to the ', 'beach' if not raining else 'library')

age = 12
s = 'minor' if age < 21 else 'adult'
print(s)
y ='yes' if 'qux' in ['foo', 'bar', 'baz'] else   'no'
print(y)

# chaining conditional expressions together
x = 3
s = ('foo' if (x == 1) else
     'bar' if (x == 2) else
     'baz' if (x == 3) else
     'qux' if (x == 4) else
     'quux'
     )




print('foo' if True else 1/0)

print(1/0 if False else 'bar')






