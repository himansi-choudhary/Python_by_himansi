# Parent class 
class Employee:
    name = "Himansi"
    salary = 100000000

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and company is {self.company}")


# Parent class
class language:
    language = "Python"

# Child Class with 2 parent class
class Programmer(Employee, language):
    company = "ITC Infotech"

    def showLanguage(self):
        print(f"{self.name} is a good with {self.language} langauge") 

a = Employee()
b = Programmer()
b.show() 
b.showLanguage()