# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sumrecursive(n):
    if n==1:
        return 1
    else:
        return n + sumrecursive(n-1)


n = int(input("Enter a n: "))

print(f"Sum of first {n} natural number: {sumrecursive(n)}")