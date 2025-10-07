# after using this, even if we change the class attribute in object we can access class attribute value
class Employee:
    a = 1
    @classmethod 
    def show(cls):
        print(f"The class attribute of a is {cls.a}")


e = Employee()
e.a = 45

e.show()




# normal
'''
class Employee:
    a = 1
    def show(self):
        print(f"The class attribute of a is {self.a}")

e = Employee()
e.a = 45

e.show()
'''