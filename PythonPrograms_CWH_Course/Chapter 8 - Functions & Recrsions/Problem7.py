# 7. Write a python function to remove a given word from a list ad strip it at the same time. 

def word(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip("an")) 
            # strip("word") :- item have "an" at start or last  will remove
            # if a or n sepratally at start or end they will also remove/strip
            # if "an is in midal it will not remove"
    return n

l = ["Himansi", "Rohan", "Ritika", "an", "adfggfn"]

print(f"New list: {word(l, "an")}")     # New list: ['Himansi', 'Roh', 'Ritik', 'dfggf']