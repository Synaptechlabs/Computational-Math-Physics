"""
sieve_eratosthenes.py - Generate all prime numbers up to a given limit using the Sieve of Eratosthenes.
Author: Scott
"""

def sieve(n):
    prime = [True] * (n+1)
    prime[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False
    return [i for i, is_prime in enumerate(prime) if is_prime]

if __name__ == "__main__":
    n = int(input("Generate primes up to: ") or "100")
    primes = sieve(n)
    print(f"Primes up to {n}: {primes}")
