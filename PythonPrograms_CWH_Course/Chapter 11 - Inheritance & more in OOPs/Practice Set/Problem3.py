# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.


# Chat gpt
class Employee:
    def __init__(self, salary):
        self.salary = salary   # Base Salary
        self.increment = 1.10  # Default increment is 10%

    @property
    def salaryAfterIncrement(self):
        # Returns salaryafter applying increment
        return int(self.salary * self.increment)
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, new_salary):
        # updates increment based on the new desired salary
        self.increment = new_salary/self.salary

emp = Employee(50000)

print(f"Old salary: {emp.salary}")
print(f"Old increment Rate: {emp.increment}")
print(f"Salary after 10% increment: {emp.salaryAfterIncrement}")


# Suppose we want the new salary to be 6000 not just 10% more
emp.salaryAfterIncrement = 60000 # This updates the increment dynamically

print()
print(f"Updated increment Rate: {emp.increment}")
print(f"Updated Salary after increment:{emp.salaryAfterIncrement}")


# Harry bhai
'''
class Employee:
    salary = 234
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment / 100))
    

    @salaryAfterIncrement.setter
    def setincement(self, salary):
        self.increment = ((salary/self.salary) - 1) * 100


emp = Employee()

emp.setincement = 280

print(emp.increment  )
'''