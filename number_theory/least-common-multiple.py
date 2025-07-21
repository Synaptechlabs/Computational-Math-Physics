"""
LCM Calculator – Least Common Multiple of Two or More Integers

This script calculates the Least Common Multiple (LCM) of two or more integers
using the classic Euclidean algorithm. Accepts space- or comma-separated input.

Author: Scott Douglass
Date: 2025-04-20
"""

from functools import reduce

def gcd(a, b):
    """Compute the GCD of two integers using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    """Compute the LCM of two integers."""
    return abs(a * b) // gcd(a, b) if a and b else 0

def lcm_list(numbers):
    """Compute the LCM of a list of integers."""
    return reduce(lcm, numbers)

def parse_input(raw):
    """
    Parses user input allowing both space- and comma-separated numbers.

    Args:
        raw (str): Raw input string

    Returns:
        list[int]: List of integers
    """
    cleaned = raw.replace(',', ' ')
    try:
        return list(map(int, cleaned.split()))
    except ValueError:
        print("❌ Invalid input. Please enter integers separated by space or commas.")
        exit(1)

if __name__ == "__main__":
    input_str = input("Enter integers (space or comma separated, default: 12 18 30): ").strip()
    numbers = parse_input(input_str) if input_str else [12, 18, 30]
    result = lcm_list(numbers)
    print(f"LCM{tuple(numbers)} = {result}")

