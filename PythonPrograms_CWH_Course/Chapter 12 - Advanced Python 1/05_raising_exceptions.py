# Sometimes you want to stop the program or give a custom error when something goes wrong — that’s where raise comes in.


age = int(input("Enter your age: "))

if age < 0:
    raise ValueError("❌ Age cannot be negative!")
else:
    print("Age is valid 👍")

