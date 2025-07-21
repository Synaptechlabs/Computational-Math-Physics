"""
integer_factorization.py - Naive trial division to factor an integer into primes.
Good educational intro to factoring.
Author: Scott
"""

def factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    if n > 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    n = int(input("Enter number to factor: ") or "84")
    print(f"Prime factors of {n}: {factorize(n)}")
