# 2. The game() function in a program lets a user play a game and returns the scoreas an integer. 
# You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. 
# You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.

import random


def game():
    print("You are playing the game...")
    score = random.randint(1,100)  # rand-int take 2 numbers and give random numbers between that 2 nums 

    # Fetch the hiscore
    with open("Hi-score_forQ2.txt") as f:
        hiscore = f.read()

        # hiscore is str, to compare score and hiscore we need to convert hiscore into int datatype
        if(hiscore != ""):
            hiscore = int(hiscore)
        else:
            hiscore = 0


    print(f" Previous High score: {hiscore}")
    print(f"Your score: {score}")

    
    # comparing and writing
    if(score > hiscore):
        #write this hiscore to the file
        with open("Hi-score_forQ2.txt", "w") as f2:
            f2.write(str(score))

    return score



game()