"""
gcd.py - Compute the Greatest Common Divisor (GCD) of two integers using the Euclidean algorithm.
Author: Scott
"""

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

if __name__ == "__main__":
    a = int(input("Enter first integer: ") or "12")
    b = int(input("Enter second integer: ") or "18")
    print(f"GCD({a}, {b}) = {gcd(a, b)}")
