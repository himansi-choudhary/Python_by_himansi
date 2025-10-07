# 1. Write a program using functions to find greatest of three numbers. 

def gretestnum(n1, n2, n3):
    if(n1 > n2 and n1 > n3):
        return n1
    elif(n2 > n1 and n2 > n3):
        return n2
    else:
        return n3


print("Enter 3 numbers: ")
n1 = int(input())
n2 = int(input())
n3 = int(input())

print(f"Greatest of 3 numbers: {gretestnum(n1, n2, n3)}")