# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

num = int(input("Enter a number: "))
table = [num * i for i in range(1, 11)]

with open("Tables.txt", "w") as file:
    for i, value in enumerate(table, start=1):
        file.write(f"{num} x {i} = {value}\n")

print("Table written to 'Tables.txt'")

