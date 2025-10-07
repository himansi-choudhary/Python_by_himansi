# 4. Write a program to display a/b where a and b are integers. 
# If b=0, display infinite by handling the ‘ZeroDivisionError’.


try:
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))

    result = a / b
    print(f"Result of {a} / {b} = {result}")

except ZeroDivisionError:
    print("infinite")


