class Emmployee:
    name = "#"
    salary = 1200000

    # dunder method hich starts which __ and is automatically called
    def __init__(self):
        print("I am creating an object ")

    def getinfo(self):
        print(f"Employyee name is {self.name}. The salary is {self.salary}")

    @staticmethod 
    def greet():
        print("Good morning")


harry = Emmployee()
harry.name = "Harry"
print(harry.name, harry.salary)



# 2nd example

class Emmployee:
    name = "#"
    salary = 0

    def __init__(self, name, salary):
        print("I am creating an object ")
        self.name = name
        self.salary = salary

    def getinfo(self):
        print(f"Employyee name is {self.name}. The salary is {self.salary}")

    @staticmethod 
    def greet():
        print("Good morning")


harry = Emmployee("Himansi", 1500000)
print(harry.name, harry.salary)