# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''



letter = '''Dear <|Name|>,
You are selected!
<|Date|>
'''

print(letter.replace("<|Name|>", "Himansi").replace("<|Date|>", "14/05/2025"))