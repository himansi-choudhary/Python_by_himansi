# Recursion is a function which calls itself. 
# It is used to directly use a mathematical formula as function. 


def factorial(n):
    if (n==1 or n ==0):
        return 1
    return n * factorial(n-1)



num = int(input("Enter a Number: "))
fact =  factorial(num)
print(f"The Factorial of a given number is {fact}")