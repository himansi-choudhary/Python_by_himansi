# 4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Entre a username:")

if(len(username) < 10):
    print("username contains less than 10 characters")
else:
    print("username not contains less than 10 characters")