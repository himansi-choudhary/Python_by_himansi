# Parent Class 
class Employee:
    a = 1

# Child class
class Programmer(Employee):
    b = 2

# Child class
class Manager(Programmer):
    c = 3


o = Employee()
print(o.a) # Employee can not acces child class data

o = Programmer()
print(o.a, o.b) # Programmer class can acces it's parent(employee) and itself data

o = Manager()
print(o.a, o.b, o.c) # Manager class can acces it parent(Programmer) data and also it's grand parent(Employee) data
