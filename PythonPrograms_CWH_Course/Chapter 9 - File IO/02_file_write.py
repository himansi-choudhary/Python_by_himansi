st = "Hey Himansi you are amazing"


# if file is not existing so it will create file and write on it
f = open("myfile.txt", "w")
f.write(st)
f.close()


'''
# if we write on existing file it will overwite, remove existing text and add new one
# in file.txt is a sentence :- Himansi is a good girl .
# after runni below code it will remove that sentence and add string name variable(st)
f = open("file.txt", "w")
f.write(st)
f.close()
'''

# to add we use append see in 03_append file