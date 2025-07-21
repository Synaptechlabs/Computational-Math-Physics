"""
lcm.py - Compute the Least Common Multiple (LCM) of two integers using the GCD.
Author: Scott
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)

if __name__ == "__main__":
    a = int(input("Enter first integer: ") or "12")
    b = int(input("Enter second integer: ") or "18")
    print(f"LCM({a}, {b}) = {lcm(a, b)}")
