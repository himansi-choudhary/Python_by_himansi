'''
a = 89

def fun():
    a = 3
    print(a)

fun()
print(a)
'''
# output :-    3
#             89





a = 89

def fun():
    global a   # if we use global then it means we make changes in global variable
    a = 3
    print(a)

fun()
print(a)

# output :-     3
#               3