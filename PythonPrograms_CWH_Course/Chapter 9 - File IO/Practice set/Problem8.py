# 8. Write a program to make a copy of a text file “this. txt”

with open("this_forQ8.txt") as f:
    content = f.read()


with open("this_forQ8_copy.txt", "w") as f:
    f.write(content)

