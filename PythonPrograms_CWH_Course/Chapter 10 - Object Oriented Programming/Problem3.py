# 3. Create a class with a class attribute a; create an object from it and set ‘a’ directly using ‘object.a = 0’.
# Does this change the class attribute?
# answer :- no (becoz change will done only in object not in class)
# code :- 

class c1:
    a = 101


obj = c1()

print(obj.a)

obj.a = 0
print(obj.a)

print(c1.a)