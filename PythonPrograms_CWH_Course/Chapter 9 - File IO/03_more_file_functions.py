f = open("file.txt")


# example 1
'''
lines = f.readlines()
print(lines, type(lines))
# output :- 
# ['Himansi is a good girl\n', 'i am a second line\n', 'a am a third line\n', 'Twinkle Twinkle tillet star'] <class 'list'>
'''


#Example 2
'''
line1 = f.readline()
print(line1, type(line1))
line2 = f.readline()
print(line2, type(line2))
line3 = f.readline()
print(line3, type(line3))
line4 = f.readline()
print(line4, type(line4))
# output:-
# Himansi is a good girl
#  <class 'str'>
# i am a second line
#  <class 'str'>
# a am a third line
#  <class 'str'>
# Twinkle Twinkle tillet star <class 'str'>
'''

# belove code also ganrate same output as 2nd ex genrated
# Example 3
'''
line = f.readline()
print(line, type(line))
line = f.readline()
print(line, type(line))
line = f.readline()
print(line, type(line))
line = f.readline()
print(line, type(line))
'''


'''
# exapmle 4: using loop
line = f.readline()
while(line != ""):   # loop will itrate until file text ends
    print(line)
    line = f.readline()

# output:-
# Himansi is a good girl

# i am a second line

# a am a third line

# Twinkle Twinkle tillet star
'''


# conclusion:- 
# varisable.readlines() : to print all lines in list form
# variable.readline(): to print 1 line at a time in string form



f.close()