"""
modular_inverse.py - Compute the modular inverse of a number under mod m, if it exists.
Author: Scott
"""

def extended_euclidean(a, b):
    if b == 0:
        return (a, 1, 0)
    else:
        g, x1, y1 = extended_euclidean(b, a % b)
        x, y = y1, x1 - (a // b) * y1
        return (g, x, y)

def mod_inverse(a, m):
    g, x, _ = extended_euclidean(a, m)
    if g != 1:
        return None  # No inverse exists
    else:
        return x % m

if __name__ == "__main__":
    a = int(input("Enter number: ") or "3")
    m = int(input("Enter modulus: ") or "11")
    inv = mod_inverse(a, m)
    if inv is None:
        print(f"No modular inverse exists for {a} mod {m}")
    else:
        print(f"Modular inverse of {a} mod {m} = {inv}")
