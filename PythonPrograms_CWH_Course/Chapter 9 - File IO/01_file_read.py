# open is a built in function which helps to open file
# Python has an open() function for opening files. It takes 2 parameters:  filename and mode. 
# open("filename", "mode of opening(read mode by default)") 
# open("this.txt", "r") read mode
# open("this.txt", "w") write mode



# to read a file

f = open("file.txt")
data = f.read()
print(data)
f.close()

# f.read =  read() is use to read a file, f = the variable in which we open a file
# f.close : whenever we open a file do work on it after completing all works it is a deuty to close that file

