# 2. Write a python program using function to convert Celsius to Fahrenheit. 

# (c* 9/5)+32

def converter(celsius):
    return (celsius * 9/5) + 32


cel = int(input("Enter Celsius: "))

print(f"Fahrenheit = {converter(cel)}")