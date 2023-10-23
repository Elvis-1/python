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