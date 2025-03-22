import math

def get_input():
    """Function to take input from the user."""
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    return a, b

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a, b):
    pass  # To be implemented by a team member

def divide(a, b):
    return a/b


def modulus(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return int(a % b)

def power(a, b):
    return a**b 


def square_root(a):
    if a < 0:
        return "Error: Cannot compute square root of a negative number."
    return math.sqrt(a)  

def factorial(a):
    fact=1
    for i in range(int(a),1,-1):
        fact*=i
    return fact

def sine(a):
    return math.sin(a)

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

def gcd(a, b):
    return math.gcd(int(a), int(b))  

def lcm(a,b):
    a=int(a)
    b=int(b)

    return abs(a*b)//gcd(a,b)

def calculator():
    print("\nWelcome to the Team Calculator!")
    a, b = get_input()  # Taking input for `a` and `b`
    print(f"Values received: a = {a}, b = {b}")
    #1st function
    print(f"Addition of {a} and {b} is {add(a,b)}")
    #2nd function
    print(f"Subtraction of {a} and {b} is {subtract(a,b)}")
    #4th function
    print(f"Division of {a} and {b} is {divide(a,b)}")
    #5th function
    print(f"Modulus of {a} and {b} is {modulus(a,b)}")
    #6th function
    print(f"{a} ** {b} is {power(a,b)}")
    #7th function
    print(f" math.sqrt {a} is {square_root(a)}")
    

    #8th function
    print(f"Factorial value of {a} is {factorial(a)}")
    print(f"Sin value of {a} is {sine(a)}.")
    #14th function
    print(f"Absolute value of {a} is {absolute(a)}")
    #12th function
    print(f"log_{b}({a}) =", logarithm(a, b))
    #15th function
    print(f"GCD of {a} and {b} is {gcd(a, b)}")
    #16th function
    print(f"LCM of {a} and {b} is {lcm(a, b)}")

    

if __name__ == "__main__":
    calculator()
