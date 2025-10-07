# 1. Write a program to open three files 1.txt, 2.txt and 3.txt 
# if any these files are not present, a message without exiting the program must be printed prompting the same.

files = ["1.txt", "2.txt", "3.txt"]

for file in files:
    try:
        with open(file, 'r') as f:
            print(f"\nContent of {file}")
            print(f.read())
            print()
    except FileNotFoundError:
        print(f"file {file} is missing")

