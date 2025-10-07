# We are going to write a program that generates a random number and asks the user to guess it.

# If the player’s guess is higher than the actual numbe the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher number please” 
# When the user guesses the correct number, 
# the program displays the number of guesses the player used to arrive at the number.

# Hint: Use the random module



import random

n = random.randint(1, 100)


a = int(input("Guess the number between 1 and 100: "))
count = 1 


while a != n:
    if a < n:
        print("Higher number please.")
    else:
        print("Lower number please.")

    a = int(input("Try again: "))
    count += 1


print("\n🎉 Hurray! You guessed the right number!") # this emoji take from gpt
print(f"You took {count} attempts.")


