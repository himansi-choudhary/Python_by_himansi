# Arithmatic Operators

a = 34
b = 4
print("Addition:",a + b)
print("Substraction:", a - b)
print("Multiplication:", a * b)
print("Division", a / b)


print()
print()


# Assignment Operator

c = 4-2   # Assign 4-2 in c
d = 6     # Assign 6 in d

print("c =", c)

d += 3    # d = d + 3 = 6 + 3 = 9
print("b+= 3 =", d)

d -= 3    # d = d - 3 = 9 - 3 = 6
print("b-= 3 =", d)

d *= 3    # d = d - 3 = 6 * 3 = 18
print("b*= 3 =", d)

d /= 3    # d = d - 3 = 18 / 3 = 6.0
print("b/= 3 =", d)



print()
print()

# Comparison Operator

e = 10
f = 15
g  = 15

equal = e == f
print(equal)   # False as e==f 10==15 is not correct

greterThan = f > e 
print(greterThan)   # True as 15 is grater Than 10

smallerThan = f < e 
print(smallerThan)   # False as 15 is not smaller Than 10

greterThanequal = f >= g
print(greterThanequal)   # True as 15 is equal to 15

smallerThanequal = f <= e 
print(smallerThanequal)   # False as 15 is not smallet than 10 and also not equal to 10


print()
print()


# Logical Operator

print("Truth Table of OR Operator:")
print("True or True is", True or True)   # T
print("True or False is", True or False)   # T
print("False or True is", False or True)   # T
print("False or False is", False or False)  # F

print("")

print("Truth Table of AND Operator:")
print("True and True is", True and True)  # T
print("True and False is", True and False)  # F
print("False and True is", False and True)  # F
print("False and False is", False and False)  # F

print("")

print("Truth Table of NOT Operator:")
print("not True is", not True)
print("not False is", not False)