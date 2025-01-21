# calculator.py
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b

def multiply(a, b):
    """Return the product of two numbers."""
    return a * b

def divide(a, b):
    """Return the quotient of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

print(add(a,b))
print(subtract(a,b))
print(multiply(a,b))
print(divide(a,b))
