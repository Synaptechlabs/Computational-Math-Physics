"""
simpsons_rule.py
Numerical integration using Simpson's Rule.
Author: Scott
"""

def f(x):
    return x**2  # Example: integrate x^2

def simpsons(a, b, n):
    if n % 2:
        raise ValueError("n must be even for Simpson's rule")
    h = (b - a) / n
    result = f(a) + f(b)
    for i in range(1, n):
        factor = 4 if i % 2 else 2
        result += factor * f(a + i * h)
    return result * h / 3

if __name__ == "__main__":
    a = float(input("Lower bound a (default 0): ") or 0)
    b = float(input("Upper bound b (default 1): ") or 1)
    n = int(input("Even number of intervals (default 100): ") or 100)
    print(f"Integral ≈ {simpsons(a, b, n):.6f}")
