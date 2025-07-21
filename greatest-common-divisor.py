#!/usr/bin/env python3
"""
Greatest Common Divisor Calculator (GCD)

This script computes the Greatest Common Divisor (GCD) of two or more integers
using the Euclidean algorithm. It supports input via the command line with
space-separated or comma-separated values.

Features:
- Default input: [48, 18, 30] if none provided.
- Validates input and handles non-integer values gracefully.
- Uses custom implementation of Euclidean algorithm.

Author: Scott
Date: 2025-07-20
"""

def gcd(a, b):
    """Compute the greatest common divisor using the Euclidean algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)

def gcd_list(numbers):
    """Compute GCD for a list of integers."""
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result = gcd(result, num)
    return result

def parse_input(input_str):
    """Convert comma or space-separated string into a list of integers."""
    try:
        cleaned = input_str.replace(',', ' ')
        return [int(x) for x in cleaned.split() if x]
    except ValueError as e:
        print(f"❌ Invalid input: {e}")
        exit(1)

def main():
    input_str = input("Enter integers (comma or space separated, default: 48 18 30): ").strip()
    numbers = parse_input(input_str) if input_str else [48, 18, 30]
    result = gcd_list(numbers)
    joined = ', '.join(str(n) for n in numbers)
    print(f"GCD({joined}) = {result}")

if __name__ == "__main__":
    main()
