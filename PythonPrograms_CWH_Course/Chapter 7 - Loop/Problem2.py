# 2. Write a program to greet all the person names stored in a list ‘l’ and which starts with S. 

l = ["Harry", "Soham", "Sachin", "Rahul"] 



for name in l:
    if(name.startswith("S")):
        print(f"Hello, {name}")


# my solution :-
'''
i = 0
while(i<len(l)):
    if(l[i][0] == "S"):
        print(f"Hello, {l[i]}")
    i += 1
'''





