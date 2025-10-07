# 1. Write a program to create a dictionary of Hindi words with values as their English translation. 
# Provide user with an option to look it up!

words = {
    "madat": "Help",
    "Namaste": "Hello",
    "Bili": "Cat"
}

word = input("Enter a word you want meaning of : ")

print(words.get(word)) # also can write print(words[word])