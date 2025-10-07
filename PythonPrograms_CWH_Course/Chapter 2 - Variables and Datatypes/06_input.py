a = input("Enter number 1 : ")
b = input("Enter Number 2 : ")

print("Sum of given two input num", a, "&", b, ":",  a+b) # suppose a=3 b=5 ans => 35
# reason :- input fuction take value in string form. and if we add two string it concate (join) the value
# therefore, as "him" + "ansi" = himansi it also concate 3" + "5" = 35




# to avoid this and calculating sum of num we have to do typeCasting
print("After Applying TypeCasting: ")


c = int(input("Enter number 1 : ")) # if user give floating value it will show error
d = int(input("Enter Number 2 : "))
print("Sum of given two input num", c, "&", d, ":", c+d)


e = float(input("Enter number 1 : "))
f = float(input("Enter Number 2 : "))
print("Sum of given two input num", e, "&", f, ":", e+f)