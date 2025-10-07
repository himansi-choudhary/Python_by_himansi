# normal Way
'''
b = int(input("Hey, Enter a number: "))
print(b)
print("Thank you")
'''
# if user input name or some rongh data type then it will crash(give error) and program will stop there will not go to next code
# which is not good, it is responsiblity of programmer to output a valid text that it is not a correct data typr or input

# so for that Exception Handling 



# way 1 of exception handling
'''
try:
    a = int(input("Hey, Enter a number: "))
    print(a)

# if all are good the a will print but if user give invalid input then 
# programe will go in except block and print what mistake you did

except Exception as e:
    print(e)

print("Thank You")
'''






# way 2

try:
    a = int(input("Hey, Enter a number: "))
    print(a)

# if all are good the a will print but if user give invalid input then 
# programe will go in except block and print what mistake you did


# we can also give exception for diffrent error ex. if we enter string into a then it is value error so:
except ZeroDivisionError as z:        # for this error search and learn by yourself
    print(z)
except ValueError as v:            # for this error search and learn by yourself
    print("Value Error")
    print(v)
except TypeError as t:         # for this error search and learn by yourself
    print(t)
except Exception as e:       # for all other error
    print(e)


print("Thank You")





