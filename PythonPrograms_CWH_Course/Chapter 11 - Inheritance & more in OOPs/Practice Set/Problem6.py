# 6. Write __str__() method to print the vector as follows:
# 7i + 8j +10k 
# Assume vector of dimension 3 for this problem.


class vector:
    def __init__(self, components):
        self.components = components # List of values like [1,2,3]
    
    def __str__(self):
        # String representation for printing
        return f"{self.components[0]}i + {self.components[1]}j + {self.components[2]}k"
    

v = vector([7, 8, 10])
print(v)