# with statement :-
# The best way to open and close the file automatically is the with statement.


# normally
f = open("file.txt")
print(f.read())
f.close()



# using with statement 
with open("file.txt") as f:
    print(f.read())


# by using with statement we don't have to explicitly close the file