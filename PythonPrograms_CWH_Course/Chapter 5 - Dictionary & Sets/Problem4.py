# 4. What will be the length of following set s:
s = set()
s.add(20)
s.add(20.0)
s.add('20') # length of s after these operations?


# answer 
print(s) 
print(len(s)) # 2

# reason 20 and 20.0 is equal same so that there are only 2 values store in a set {'20', 20}
