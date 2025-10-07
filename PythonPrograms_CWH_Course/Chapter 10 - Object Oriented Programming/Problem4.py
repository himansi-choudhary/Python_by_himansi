# 4. Add a static method in problem 2, to greet the user with hello.

import math

class calculator:
    num = 0

    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"Square of num is {self.num**2}")

    def cube(self):
        print(f"Cube of a number is {self.num**3}")

    def squareroot(self):
        print(f"Square root of number is {math.sqrt(self.num)}") # ithou math method formula = self.num**1/2

    # using static method
    @staticmethod
    def greet():
        print("Hello")


num = calculator(4)
num.greet()
num.square()
num.cube()
num.squareroot()