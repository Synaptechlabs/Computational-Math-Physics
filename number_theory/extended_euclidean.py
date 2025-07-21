"""
extended_euclidean.py - Find integers x and y such that ax + by = gcd(a, b)
Author: Scott
"""

def extended_euclidean(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        gcd, x1, y1 = extended_euclidean(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return (gcd, x, y)

if __name__ == "__main__":
    a = int(input("Enter first integer: ") or "99")
    b = int(input("Enter second integer: ") or "78")
    g, x, y = extended_euclidean(a, b)
    print(f"GCD({a}, {b}) = {g} with x = {x}, y = {y} -> {a}*{x} + {b}*{y} = {g}")
