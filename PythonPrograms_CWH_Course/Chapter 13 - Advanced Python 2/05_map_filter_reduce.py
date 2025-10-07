from functools import reduce


# Map 
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)

print(sqList)    # it will give address

print(list(sqList))  # it will give list




# Filter
def even(n):
    if(n%2 == 0):
        return True
    return False


onlyEven = filter(even, l)
print(list(onlyEven))  # [2, 4]




# Reduce
def sum(a, b):
    return a+b

print(reduce(sum, l))


'''
1  2  3  4  5
3  3  4  5  
6  4  5
10  5
15
'''