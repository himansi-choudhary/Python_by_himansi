# 5. Write a program to find the maximum of the numbers in a list using the reduce function.

from functools import reduce

l = [1, 2, 3424, 53, 355, 65, 340, 20, 111]


def greater(a, b):
    if(a > b):
        return a
    return b

print(reduce(greater, l))