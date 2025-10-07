# 1st
'''
def myFunc():
    print("Hello World!")

myFunc()

print(__name__)
'''

# this file is imported to 08_main.py and if we run print(__name__)
# if we run 08_main.py then out put will == module
# ad if i run this file then output == __main__  

# 2nd
def myFunc():
    print("Hello World!")



if __name__ =="__main__":
    # if this code is directly executed by running the file its present in
    print("We are directly running this code")
    myFunc()
    print(__name__)