# every method no need to  store in new variable 
# this changes will do in orignal list 

friends = ["Apple", "Oreange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)


# append(new element) : add new element at the end
friends.append("Himansi")
print(friends)


# reverse : it reverse the list
friends.reverse()
print(friends)


# sort() : only sort numeric list
l1 = [1, 67, 90, 33, 2, 56, 66]
l1.sort()
print(l1)  # [1, 2, 33, 56, 66, 67, 90]



# insert(index, value) : insert value at index
l1.insert(3, 8)  # This will add 8 at 3 index
print(l1)    # [1, 2, 33, 8, 56, 66, 67, 90]


#
valuepoped = l1.pop(2)  # Will delete element at index 2 and return its value.
print(valuepoped)  # output : 33  .:.( and final list will [1, 2, 8, 56, 66, 67, 90] )
print(l1)

#
l1.remove(66) # Will remove 66 from the list. 
print(l1)   # [1, 2, 8, 56, 67, 90]


#
l = [10, 45, 30, 15]
print(sum(l))