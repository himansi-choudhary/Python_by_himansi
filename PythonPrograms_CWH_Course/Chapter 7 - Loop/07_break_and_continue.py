# THE BREAK STATEMENT 
# ‘break’ is used to come out of the loop when encountered. 
# It instructs the program to – exit the loop now. 

for i in range(50):
    if(i==34):
        break  # Exit the loop so after this for will print 0 - 33
    print(i)  
print("\n\n")





# THE CONTINUE STATEMENT 
# ‘continue’ is used to stop the current iteration of the loop and continue with the next one. 
# It instructs the Program to “skip this iteration”. 


for i in range(50):
    if(i==34):
        continue  # this will skip one itration. when value will 34 it will skip for loop body and increament to 35 
    print(i)  #  prints 0-50 but skips 34. 34 will not print






# PASS STATEMENT 
# pass is a null statement in python. 
# It instructs to “do nothing”. 

l = [1,7,8] 
for item in l: 
    pass         