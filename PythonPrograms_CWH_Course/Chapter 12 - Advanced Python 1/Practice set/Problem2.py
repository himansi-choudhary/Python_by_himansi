# 2. Write a program to print third, fifth and seventh element from a list using enumerate function.

l = ["E1", "E2", "E3", "E4", "E5", "E6", "E7"]

for index, item in enumerate(l):
    if index in [2, 4, 6]:  # 3rd, 5th, and 7th items
        print(f"Element {index + 1}: {item}")

