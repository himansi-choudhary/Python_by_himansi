# What is the Walrus Operator in Python?
# The walrus operator := allows you to assign a value to a variable as part of an expression.
# It's also called the assignment expression operator.
# Introduced in Python 3.8+


# Ex. 1 - Using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)

# With walrus (shorter & cleaner)
while (data := input("Enter data: ")) != "exit":
    print(f"You entered: {data}")



'''
# Ex. 1 - Without walrus
n = [1, 2, 3, 4, 5]
n1 = len(n)
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n1} elements, expected <= 3)")
# Output: List is too long (5 elements, expected <= 3)


# Ex. 2 -  Without walrus
data = input("Enter data: ")
while data != "exit":
    print(f"You entered: {data}")
    data = input("Enter data: ")
'''