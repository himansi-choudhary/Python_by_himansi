marks = {
    "Himansi": 100,
    "Ritika": 100,
    "Harry": 110
}

print(marks.items())   # dict_items([('Himansi', 100), ('Ritika', 100), ('Harry', 110)])



# dict.keys(): Returns a list containing dictionary's keys.
print(marks.keys())  # dict_keys(['Himansi', 'Ritika', 'Harry'])



# dict.values(): Returns a list containing dictionary's values.
print(marks.values())  # dict_values([100, 100, 110])



# update
marks.update({"Himansi": 105, "renuka": 98})  # ex1: existing key upadte value ex2: adding new key:value
print(marks)



print(marks.get("Himansi"))  # 105  
# but below is also giving same ans
print(marks["Himansi"]) # 105

# let's see diffrence  by key which not exist in dictionary
print(marks.get("Himansi2")) # Prints none

print(marks["Himansi2"]) # Returns an error


# more methods by gpt
# pop 
# pop item
# len