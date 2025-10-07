# 5. Write a program which finds out whether a given name is present in a list or not.

list = ["Himansi", "Ritika", "Urmila", "Gourav"] 

searchname = input("Entre name to search: ")

if(searchname in list):
    print("Name found in list")
else:
    print("Name not found in list")