try:
    a = int(input("Hey, Enter a number: "))
    print(a)

except Exception as e:
    print(e)

finally:
    print("I am Inside finally")

# here a quetion arries that finally run no matter what is done so why we write finally 
# some thing is happing without writing finally

# so finally manlly is used/usefull for function

# ex in thisa we have seen previously that if inside function the code return then below code not execute 
# but if we write finally it is compalsory to no matter what statement executes  
# and full explainaion is in notes file (part-2)

def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return
    
    except Exception as e:
        print(e)
        return
    
    finally:
        print("I am Inside finally")


main()