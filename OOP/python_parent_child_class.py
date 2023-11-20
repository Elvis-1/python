class Employees:
    def __init__(self,name, last) -> None:
        self.name = name
        self.last = last

class Supervisors(Employees):
    def __init__(self, name, last,password) -> None:
        super().__init__(name, last)
        self.password = password

class Chefs(Employees):
    def leaveRequest(self, days):
        return "May I take a leave for " + str(days) + " days?"
    

adrian = Supervisors("Andrian","A","apple")

emily = Chefs("Emily",'E')
juno = Chefs("Juno","J")

print(emily.leaveRequest(3))
print(adrian.password)
print(emily.name)