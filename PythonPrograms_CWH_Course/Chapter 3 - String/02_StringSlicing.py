#  string Slicing

a = "Himansi"
nameshort = a[0:4]
print(nameshort) # it will take character from string :- from 0 index to 3 , 4 will exclude

character1 = a[0]
print(character1) # if we have to print 1 character than only write that characters index value





# Negative Slicing

#  H    i    m    a    n    s    i
#  0    1    2    3    4    5    6    
# -7   -6   -5   -4   -3   -2   -1

print(a[-4 : -1]) # ans

# going hard then convert in positive example:- -4 = 3 and -1 = 6
print(a[3:6]) # ans





# [first index : last index] 
# if we don't write first index [:4] means [0:4]
# if we don't write last index [1:] means [1:length] all character till end. example : - a lenght 7 so [1:7]

print(a[:4])

print(a[1:])





# SLICING WITH SKIP VALUE

b = "0123456789"

skip = b[1: 7: 2]  # first : it will take charactor from index 0-6 as 7 will exclude so skip = "123456"
# now count start and (jaha bhi 2 aaye wo lenge )
# ex. 1
# 2[1] 3[2]  ....... 3
# 4[1] 5[2]  ....... 5
# 6[1] and end so stop 
# ans is 1, 3, 5


print(skip) # 135


# also with word

word = "Amazing"
print(word[1: 6: 2]) # first[1:6] = "mazin" second[2] = mzn