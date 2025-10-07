# 4. Write a program to find whether a given number is prime or not. 

num = int(input("Enter number : "))


# yaha pe num - 1 and num ke alawa divide nahi hota 
# to ye range me humne 1 and num ko chodke check karenge agar ho jaye to wo prime nahi hai
for i in range(2,num):  
    if(num%i==0):
        print(f"{num} is not a prime")
        break
else:
    print(f"{num} is prime")