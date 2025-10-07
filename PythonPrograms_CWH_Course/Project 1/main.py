import random
'''
1 for snake
-1 for water
0 for gun
'''
print()

computer = random.choice([-1, 0, 1])
print("enter s, w or g :- s = snake, w = water and g = gun :-")
youstr = input("Enter your Choice(s/w/g): ")
youDict = {
    "s" : 1,
    "w" : -1,
    "g" : 0
}

print()
print("Result")
print(f"You = {reverseDict[you]} \ncomputer = {reverseDict[computer]}")


if(computer == you):
    print("tie!, nice try keep it up")
else:
    if(computer == -1 and you == 1):             # water  snake  = y
        print("hurrey, you win!")
    elif(computer == -1 and you == 0):           # water gun  = n
        print("you loss, Better luck next time")
    elif(computer == 1 and you == 0):          # snake  gun = y
        print("hurrey, you win!")
    elif(computer == 1 and you == -1):         # snake water = n
        print("you loss, Better luck next time")
    elif(computer == 0 and you== 1):          # gun  snake   = n
        print("hurrey, you win!")
    elif(computer == 0 and you == -1):      # gun water = y
        print("you loss, Better luck next time")
    else:
        print("Something went wrong")

print()