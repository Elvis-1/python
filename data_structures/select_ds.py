# Each data structure offers a different approach to storing, accessing and updating the information stored inside it

# Example: Employees list
# In this example, there's a list of employees that work in a restaurant. You need to be able to find an employee by their employee ID - an integer-based numeric ID.

# list of tuples

employee_list = [(12345, "John", "Kitchen"), (12458, "Paul", "House Floor")] 

def getEmployeeId(id):
    for employee in employee_list:
        if employee[0] == id:
            # return
            return {'id':employee[0], 'Name':employee[1], 'Location':employee[2]} 

# print(getEmployeeId(12345))

# using dictionary ds
employee_list_dict = {
    12345:{'id':12345, 'Name':"John", 'Department':"Kitchen"},
    12346:{'id':12346, 'Name':"Paul", 'Department':"House Floor"},
    }

def getEmployeeId(id):
    return employee_list_dict[id]



# using tuples
employee_list = ({'id':12345, 'Name':"John", 'Department':"Kitchen"},{'id':12346, 'Name':"Paul", 'Department':"House Floor"})

def getEmployeeById(id):
    for employee in employee_list:
       if employee['id'] == id:
           return employee

print(getEmployeeById(12346))


