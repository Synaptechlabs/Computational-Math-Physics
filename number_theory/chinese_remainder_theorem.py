"""
chinese_remainder_theorem.py - Solve a system of modular congruences using the Chinese Remainder Theorem (CRT).
Author: Scott
"""

def extended_euclidean(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_euclidean(b, a % b)
    return g, y1, x1 - (a // b) * y1

def chinese_remainder(n, a):
    prod = 1
    for ni in n:
        prod *= ni
    result = 0
    for ni, ai in zip(n, a):
        p = prod // ni
        _, inv, _ = extended_euclidean(p, ni)
        result += ai * inv * p
    return result % prod

if __name__ == "__main__":
    print("Solving system:")
    print("x ≡ a1 mod n1")
    print("x ≡ a2 mod n2")
    print("...")
    n = list(map(int, input("Enter moduli (n) separated by spaces: ") or "3 5 7".split()))
    a = list(map(int, input("Enter remainders (a) separated by spaces: ") or "2 3 2".split()))
    print(f"Solution x ≡ {chinese_remainder(n, a)} mod {eval('*'.join(map(str,n)))}")
