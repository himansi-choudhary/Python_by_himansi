# 6. Write a program to mine a log file and find out whether it contains ‘python’.

with open("log_forQ6.txt") as f:
    content = f.read()

if("python" in content):
    print("Yes python is presnt")
else:
    print("No python is not presnt")
    