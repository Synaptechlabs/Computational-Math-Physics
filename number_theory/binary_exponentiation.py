"""
binary_exponentiation.py - Fast modular exponentiation using exponentiation by squaring.
Used in cryptography (e.g. RSA).
Author: Scott
"""

def mod_exp(base, exponent, mod):
    result = 1
    base %= mod
    while exponent > 0:
        if exponent % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exponent //= 2
    return result

if __name__ == "__main__":
    base = int(input("Base: ") or "4")
    exponent = int(input("Exponent: ") or "13")
    mod = int(input("Modulus: ") or "497")
    print(f"{base}^{exponent} mod {mod} = {mod_exp(base, exponent, mod)}")
