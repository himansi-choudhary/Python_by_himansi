# 3. Write a list comprehension to print a list which contains the multiplication table of a user entered number.


num = int(input("Enter a number: "))

table = [num * i for i in range(1, 11)]

print(f"\nMultiplication table of {num}:")
print(table)

# Table like formate
'''
for i, val in enumerate(table, start=1):
    print(f"{num} x {i} = {val}")

'''
