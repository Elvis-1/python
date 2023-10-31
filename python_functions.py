bill = 165.00
tax_rate = 75

total_tax = (bill*tax_rate)/100.00

print("Total tax", total_tax)

def calculate_tax(bill, tax_rate):
    return (bill*tax_rate)/100.00

print("Total tax: ", calculate_tax(174.00, 12))
