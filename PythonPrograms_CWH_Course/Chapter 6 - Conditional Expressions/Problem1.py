# 1. Write a program to find the greatest of four numbers entered by the user.

n1 = int(input("Enter number:"))
n2 = int(input("Enter number:"))
n3 = int(input("Enter number:"))
n4 = int(input("Enter number:"))

if(n1>n2 and n1>n3 and n1>n4):
    print(f"{n1} is Greatest Number")
elif(n2>n1 and n2>n3 and n2>n4):
    print(f"{n2} is Greatest Number")
elif(n3>n1 and n3>n2 and n3>n4):
    print(f"{n3} is Greatest Number")
else:
    print(f"{n4} is Greatest Number")