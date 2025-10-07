# 7. Override the __len__() method on vector of problem 5 to display the dimension of the vector.

class vector:
    def __init__(self, components):
        self.components = components 
    
    def __str__(self):
        return f"vector({self.components})"
    
    def __len__(self):
        # Return the dimention (number of element) of the vector
        return len(self.components)
    

v = vector([1, 2, 3])
print(f"Vector: {v}") 
print(f"Dimension: {len(v)}")

