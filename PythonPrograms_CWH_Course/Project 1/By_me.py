import random

print()
computer = random.choice(["Snake", "Water", "Gun"])
print("enter  s = snake, w = water and g = gun and for exit = e:-")
you = input("Enter your Choice(s/w/g): ")


while(you != "e"):

    youDict = {
        "s": "Snake",
        "w" : "Water",
        "g" : "Gun"
    }
    reverseDict={
        "s": "Snake",
        "w" : "Water",
        "g" : "Gun"
    }

    print()
    print("***** Result *****")
    print(f"You = {youDict[you]} \ncomputer = {reverseDict[computer]}")


    if(computer == you):
        print("tie!, nice try keep it up")
    else:
        if(computer == "w" and you == "s"):             
            print("hurrey, you win!")
        elif(computer == "w" and you == "g"):         
            print("you loss, Better luck next time")
        elif(computer == "s" and you == "g"):       
            print("hurrey, you win!")
        elif(computer == "s" and you == "w"):         
            print("you loss, Better luck next time")
        elif(computer == "g" and you== "s"):          
            print("you loss, Better luck next time")
        elif(computer == "g" and you == "w"):      
            print("hurrey, you win!")
        else:
            print("Something went wrong")

    print("----------------------------------------------------")
    print("Enter Choice: ")
    you = input("Enter your Choice(s/w/g): ")
print()
print("|-------------------------------- Thank You, For playing! --------------------------------|")
print("")