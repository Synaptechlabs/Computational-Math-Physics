"""
primality_test.py - Check if a number is prime using basic trial division.
Not efficient for large numbers but useful for educational purposes.
Author: Scott
"""

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    n = int(input("Enter integer to check for primality: ") or "29")
    print(f"{n} is prime." if is_prime(n) else f"{n} is not prime.")
