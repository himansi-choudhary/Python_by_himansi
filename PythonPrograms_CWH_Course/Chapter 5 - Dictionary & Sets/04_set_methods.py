s = {1, 5, 32, 53, 5, 12, 5, 53, "Himansi"}

print(s, type(s))  # {32, 1, 5, 53, 'Himansi', 12} <class 'set'>


# add method
s.add(566)
print(s)   # {32, 1, 5, 53, 566, 'Himansi', 12}


# 
print(len(s)) # 7


s.remove(1)
print(s)  # {32, 5, 53, 566, 'Himansi', 12}

# using s.pop is not good to use bcoz remove randomly
# s.pop() : Removes an arbitrary element from the set and return the element removed.
# print(s) 

s.clear() # empties the set s.
print(s) # set()