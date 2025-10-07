# 6. Write a python function which converts inches to cms.

2.54

def intocm(inches):
    return inches * 2.54


inches = int(input("Enter inches:"))

print(f"inches to cm : {intocm(inches)}")