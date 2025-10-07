# @property AND @.GETTERS AND @.SETTERS
# The method name with ‘@property’ decorator is called getter method.
# We can define a function + @ name.setter decorator


class Employee:

    @property  # this is also called gatter method
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        self.fname = value.split(" ")[0] 
        self.lname = value.split(" ")[1]
        # .split will split name into 2 where space Himansi|space|Choudhary
        # after spliting this name in list = ["Himansi", "Choudhary"] 
        # so in list first name is at 0 index and last name at 1 index

e = Employee()

e.name = "Himansi Choudhary"
print(e.name)


# 

'''
Q. What is @property in python?
--> ~ @property is a decorator used to make a method behave like an attributr.
    ~ it allows cotrolled access to class attribute without directly exposing the.

Q. Why use @property, @<property_name>.setter ?
    ~ To encapsulate your class fields.
    ~ To perform validation or logic when getting or setting an attribute.
    ~ Makes the syntax clean and Pythonic.
'''

# Example with code + Explaination

class Student:
    def __init__(self, name):
        self._name = name # name is a protected variable

    @property
    def name(self):
        # This will be accesed like an attribute
        print("Getting name...")
        return self._name

    @name.setter
    def name(self, value):
        # This method is called when you assign a value to `name`
        print("Setting name...")
        if len(value) < 3:
            print("Name is too short!")
        else:
            self._name = value


# Create a student object
s = Student("Himansi")

# Get the name (calls the getter)
print(s.name) # output: Getting name... Himansi

# Set the name (calls the setter)
s.name = "Hi"  # output: setting name... Name is too short!

s.name = "Aarushi" # Output: Setting name... 

# Check the updated name
print(s.name) # Output: Getting name... Aarushi