# 2. Write a class “Calculator” capable of finding square, cube and square root of a number.
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


num = calculator(4)
num.square()
num.cube()
num.squareroot()