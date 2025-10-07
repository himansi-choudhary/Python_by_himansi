# 9. Write a program to find out whether a file is identical & matches the content of another file.

with open("this_forQ8.txt") as f:
    content1 = f.read()

with open("this_forQ8_copy.txt") as f:
    content2 = f.read()

if(content1 == content2):
    print("Yes this files is identical")
else:
    print("No this files is identical")
