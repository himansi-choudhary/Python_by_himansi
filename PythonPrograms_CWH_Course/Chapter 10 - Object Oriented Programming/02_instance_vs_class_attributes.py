# Note: Instance attributes, take preference over class attributes during assignment & retrieval
# so see in class name = # but after assingning in intance(object) atribute it change value
class Emmployee:
    name = "#"
    language = "Py"
    salary = 1200000


harry = Emmployee()
harry.name = "Harry" # This is an instance(object) attribute
print(harry.name, harry.language, harry.salary)



rohan = Emmployee()
print(rohan .name, harry.language, harry.salary)