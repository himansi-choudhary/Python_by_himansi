# 1. Create a class “Programmer” for storing information of few programmers working at Microsoft.

class programmer:
    name = ""
    workingAt = "Microsoft"
    salary = 0
    position = ""


    def __init__(self, empno, name, salary, position):
        print(f"Creating object for employee {empno}...")
        self.empno = empno
        self.name = name
        self.salary = salary
        self.position = position


    def getdata(self):
        print(f"Name: {self.name} \nSalary: {self.salary} \nPosition: {self.position}")
    

Himansi = programmer(1, "Himansi", 15000000, "Cyber Scurity")
Himansi.getdata()

Ritika = programmer(2, "Ritika", 10000000, "Data analytics")
Ritika.getdata()

Urmila = programmer(3, "Urmila", 5000000, "Project managment")
Urmila.getdata()

Gourav = programmer(4, "Gourav", 200000000, "Assi.CEO")
Gourav.getdata()
