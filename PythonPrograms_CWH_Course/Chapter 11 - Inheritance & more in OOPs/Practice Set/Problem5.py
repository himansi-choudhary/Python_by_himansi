# 5. Write a class vector representing a vector of n dimensions. 
# Overload the + and * operator which calculates the sum and the dot(.) product of them.


# Basically
class vector:
    def __init__(self, components):
        self.components = components # List of values like [1,2,3]

    def __add__(self, other):
        # Add Two vectors element-wise
        result = []
        for i in range(len(self.components)):
            result.append(self.components[i] + other.components[i])
        return vector(result)
    
    def __mul__(self, other):
        # Dot product: a1*b1 + a2*b2 + a3*b3...
        result = 0
        for i in range(len(self.components)):
            result += self.components[i] * other.components[i]
        return result # dot product is scalar
    
    def __str__(self):
        # String representation for printing
        return f"vector({self.components})"
    

v1 = vector([1, 2, 3])
v2 = vector([4, 5, 6])

# vector addition
print(f"v1 + v2 = {v1 + v2}") # vector([5, 7, 9])

# Dot product
print(f"v1 * v2 = {v1 * v2}") # 32 :- (1*4 + 2*5 + 3*6)




# in Advance
'''
class vector:
    def __init__(self, components):
        self.components = components # List of values like [1,2,3]

    def __add__(self, other):
        # vector addition: [a1,a2] + [b1,b2] = [a1+b1, a2+b2]
        result = [a + b for a,b in zip(self.components, other.components)]
        return vector(result)
    
    def __mul__(self, other):
        # Dot product: a1*b1 + a2*b2 + a3*b3...
        result = sum(a * b for a,b in zip(self.components, other.components))
        return result # dot product is scalar
    
    def __str__(self):
        # String representation for printing
        return f"vector({self.components})"
    

v1 = vector([1, 2, 3])
v2 = vector([4, 5, 6])

# vector addition
print(f"v1 + v2 = {v1 + v2}") # vector([5, 7, 9])

# Dot product
print(f"v1 * v2 = {v1 * v2}") # 32 :- (1*4 + 2*5 + 3*6)
'''