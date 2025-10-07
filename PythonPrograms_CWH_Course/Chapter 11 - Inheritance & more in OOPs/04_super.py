# in normal there are runing constructur step wise
# but sometime we want thet along with manager constructor, it's parent constructore will also run
# so for that we use super method

# using super method
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a) 

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c) 




# normal
'''
class Employee:
    def __init__(self):
        print("Constructor of Employee")
    a = 1

class Programmer(Employee):
    def __init__(self):
        print("Constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        print("Constructor of Manager")
    c = 3

o = Employee()
print(o.a) 

o = Programmer()
print(o.a, o.b)

o = Manager()
print(o.a, o.b, o.c) 
'''