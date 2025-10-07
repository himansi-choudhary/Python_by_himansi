age = int(input("Enter your age: "))


# if statement 1
if(age%2 == 0):
    print(f"{age} even ")
# End of if statement 1

#if statement 2
if(age>=18):
    print("You are allow to vote")
elif(age<0):
    print("Invalid age")
else:
    print("You are not allow to vote")
# End of if statement 2

print("End of program!")