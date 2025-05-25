# Task 1: Calculate Factorial Using a Function

def factorial(n):
    if n<2:
        return 1
    else:
        return n*factorial(n-1)

inp=int(input("Enter a number: "))
print("factorial of the number",inp,"is:",factorial(inp))