# so if i want all the methods and instances of a particular classin anoter class so we inherit

# inheritance

# Parent class 
class Employee:
    name = "Himansi"
    salary = 100000000
    company = "ITC"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and company is {self.company}")


# Child Class
class Programmer(Employee):
    company = "ITC Infotech"
    language = "Python"

    def showLanguage(self):
        print(f"{self.name} is a good with {self.language} langauge") # name is in employee class as we inhrite so we can use it

a = Employee()
b = Programmer()
# show() method is in employee method but using inheritance child class ka acces all data of parent class
# b.show() company name will print "ITC Infotech" # if we do a.show() then company = "ITC"
b.show() 
b.showLanguage()





# same program in Normal form hich is landy and
'''
class Employee:
    name = "Himansi"
    salary = 100000000
    company = "ITC"
    
    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and company is {self.company}")


class programmer:
    name = "Himansi"
    salary = 100000000
    language = "python"
    company = "ITC Infotech"

    def show(self):
        print(f"The name is {self.name} and the salary is {self.salary} and company is {self.company}")

    def showLanguage(self):
        print(f"{self.name} is a good with {self.language} langauge")



a = Employee()
b = programmer()

print("Printing 1st class:-")
a.show()

print("Printing 2nd class:-")
b.show()
b.showLanguage()
'''