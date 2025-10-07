# 11. Write a python program to rename a file to “renamed_by_ python.txt.


# importing os module to work with yhe operating system
import os

# Old file name(this file should already exist in the same folder as the txt)
old_filename = "python.txt"


new_filename = "renamed_by_ python.txt"

# os.rename() is used to rename the file
os.rename(old_filename, new_filename)

print("File renamed successfullty.")
