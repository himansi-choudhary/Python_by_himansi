# 1.string length function 
a = "Himansi"
print(len(a))


# 2. String.endswith("nsi") : - string ends with // casensetive H and h is diffrent
print(a.endswith("nsi")) # True
print(a.endswith("arry")) # False


# 3. String.startswith("nsi") : - string starts with casesensetive
print(a.startswith("Hima")) # True  
print(a.startswith("Har")) # False


# 5.Capitals the first character of a given string.
str = "harry is teacher"
capitalized_string = str.capitalize()
print(capitalized_string) # Output: "Harry is teacher" only first word of sentence


# 6. string.upper() to convert all charactor into upper charactors
print(a.upper())


# 7.string.lower() to convert all charactor into lower charactors
print(a.lower())


# 8.string.count("charactor") – counts the total number of occurrences of any character.
print(str.count("a")) 


# 9.string.find(word) – This function friends a word and returns the index of first occurrence of that word in the string.
print(str.find("is")) # will return index


# 10.string.replace (old word, new word ) – This function replace the old word with new word in the entire string.
print( str.replace("a", "P") )