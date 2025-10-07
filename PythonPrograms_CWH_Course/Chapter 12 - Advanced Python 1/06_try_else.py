# Sometimes we want to run a piece of code when try was successful.
# if line 4,5 will run succesfully then it will execute else block

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am Inside else")