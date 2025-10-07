# self is mandatory to functions 
class Emmployee:
    name = "#"
    salary = 1200000

    def getinfo(self):
        print(f"Employyee name is {self.name}. The salary is {self.salary}")

    # if we don't need object attributes we use static method
    # fuction greet not accpect attributes like name salary so insted of giving whole object using self we use staticmethod
    @staticmethod 
    def greet():
        print("Good morning")


harry = Emmployee()
harry.name = "Harry" # This is an instance(object) attribute
harry.greet()
harry.getinfo()  # == Employee.getinfo(harry)


# error code
'''
class Emmployee:
    language = "Py"
    salary = 1200000

    def getinfo():
        print(f"The langauge is {language}. The salary is {salary}")

    def greet():
        print("Good morning)


harry = Emmployee()
harry.getinfo()  # == Employee.getinfo(harry)
harry.greet()
'''