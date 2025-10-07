# 1. Write a program to read the text from a given file ‘poems.txt’ 
# and find out whether it contains the word ‘twinkle’.


f = open("poem_forQ1.txt", "r")
c = f.read()
if("twinkle" in c):
    print("Yes this text file contains twinkle word")
else:
    print("No this text file doesn't contains twinkle word")

f.close()