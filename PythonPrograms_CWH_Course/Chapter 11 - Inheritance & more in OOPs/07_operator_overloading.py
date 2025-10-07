# OPERATOR OVERLOADING IN PYTHON
# Operators in Python can be overloaded using dunder methods.
# These methods are called when a given operator is used on the objects.
# Operators in Python can be overloaded using the following methods:


# p1+p2 # p1.__add__(p2)
# p1-p2 # p1.__sub__(p2)
# p1*p2 # p1.__mul__(p2)
# p1/p2 # p1.__truediv__(p2)
# p1//p2 # p1.__floordiv__(p2)



class Number:
    def __init__(self, n):
        self.n = n

    def __add__ (self, num):
        return self.n + num.n
    
    def __sub__ (self, num):
        return self.n - num.n
    
    def __mul__ (self, num):
        return self.n * num.n
    
    def __truediv__ (self, num):
        return self.n / num.n
    
    def __floordiv__ (self, num):
        return self.n // num.n
    
    def __mod__ (self, num):
        return self.n % num.n
    
    def __eq__ (self, num):
        return self.n == num.n
    
    def __lt__ (self, num):
        return self.n < num.n
    
    def __gt__ (self, num):
        return self.n > num.n
    
    def __le__ (self, num):
        return self.n <= num.n
    
    def __ge__ (self, num):
        return self.n >= num.n
    

a = Number(10)
b = Number(5)

print(f"a = {a.n} and b = {b.n}")
print("-------------------------------------")
print(f"Addition: {a + b}")   # 15
print(f"Substraction: {a - b}")   # 5
print(f"Multiplication: {a * b}")   # 50
print(f"Division: {a / b}")   # 2.0
print(f"Floor Division: {a // b}")   # 2 :- ex.if a=7, b=2 after division 7/2= 3.5 but if we use floor division the ans wiil 3
print(f"Modulus: {a % b}")   # 0
print(f"Equality: {a == b}")   # False
print(f"a Less Than b: {a < b}")   # False
print(f"a Greater Than b: {a > b}")   # True
print(f"a Less Than or Equal b: {a <= b}")   # False
print(f"a Less Than or Equal b: {a >= b}")   # True


# Other dunder/magic methods in Python:
# str__() # used to set what gets displayed upon calling str(obj) and it runs when you use print() on an object
# __len__() # used to set what gets displayed upon calling.__len__() or len(obj)