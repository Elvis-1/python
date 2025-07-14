# CONDITIONALS

# This reading introduces you to the conditional statements of if, else and elif.

# If
# In keeping with the light switch example, the state of the switch can be stored with a Boolean value of True or False.

# On = True

# Off = False

current = True

# if current:
#     current = False
#     print('Turning off current : {}'.format(current))
# if not current:
#     current = True
#     print('Turning on current : {}'.format(current))

# if else

if current:
    current = False
    print('Off')
else:
    current = True
    print('On')


# elif

loyaltyCustomer = False
billTotal = 90

if loyaltyCustomer and billTotal > 100:
    # apply 20% discount
    billTotal = billTotal + float(124 * 20/100)
elif billTotal > 100:
    # apply 10% discount
    billTotal = billTotal + float(124 * 10/100)

else:
    # sorry no discount applied
    print("Sorry ... no discount")

print('Bill total: {}'.format(billTotal))
print('Bill total 2 '+ str(billTotal))

