# To check Data Type of a variable :- type(variable_name)


a = 31
print(type (a)) # <class 'int'>

b = "31"
print(type (b)) # <class 'str'>

c = 31.45
print(type (c)) # <class 'float'>

d = True
print(type (d)) # <class 'bool'>

e = None
print(type(e)) # <class 'NoneType'>




# A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another.
# functions :- str() , int() , float()

f = float(b) # string to float of a variable data 31.0
print(type(f)) # <class 'float'>

str(31)  # integer to string conversion =>"31"
int("32")  # string to integer conversion => 32
float(32) # integer to float conversion => 32.0
