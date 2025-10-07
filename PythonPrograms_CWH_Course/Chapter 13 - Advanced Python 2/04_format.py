# in 1st{} it is harry and at 2nd{} boy
# by default numbering in {}
# a = "{0} is a good {1}".format("harry", "boy")  0 meas 0th indes == harry,.....
a = "{} is a good {}".format("harry", "boy")

b = "{1} is a good {0}".format("harry", "boy")


print(a)
print(b)





# error 
'''
c = "{1} is a good {2}".format("harry", "boy")
print(c)
'''