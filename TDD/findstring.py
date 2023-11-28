def ispresent(person):
    names = ["A1","B2","CH2","N7"]
    if person in names:
        return True
    else:
        return False
    
def nodigit(person):
    if person.isalpha():
        return True
    else:
        return False