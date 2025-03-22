import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    pass  # To be implemented by a team member

def subtract(a, b):
    pass  # To be implemented by a team member

def multiply(a, b):
    pass  # To be implemented by a team member

def divide(a, b):
    pass  # To be implemented by a team member

def modulus(a, b):
    pass  # To be implemented by a team member

def power(a, b):
    pass  # To be implemented by a team member

def square_root(a):
    pass  # To be implemented by a team member

def factorial(a):
    fact=1
    for i in range(int(a),1,-1):
        fact*=i
    return fact

def sine(a):
    pass  # To be implemented by a team member

def cosine(a):
    pass  # To be implemented by a team member

def tangent(a):
    pass  # To be implemented by a team member

def logarithm(a, b):
    return math.log(a, b)

def exponent(a):
    pass  # To be implemented by a team member

def absolute(a):
    return abs(a)

def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()  # Taking input for `a` and `b`
    print(f"Values received: a = {a}, b = {b}")
    #5th function
    print(f"Factorial value of {a} is {factorial(a)}")
    #14th function
    print(f"Absolute value of {a} is {absolute(a)}")
    #12th function
    print(f"log_{b}({a}) =", logarithm(a, b))
    

if __name__ == "__main__":
    calculator()
