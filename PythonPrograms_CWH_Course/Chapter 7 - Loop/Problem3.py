# 3. Attempt problem 1 using while loop. 
# problem 1. Write a program to print multiplication table of a given number.

n = int(input("ENter number: "))
i = 1

while(i<=10):
    print(f"{n} X {i} = {n*i}")
    i +=1