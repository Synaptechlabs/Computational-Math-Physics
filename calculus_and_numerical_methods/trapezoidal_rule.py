"""
trapezoidal_rule.py
Numerical integration using the Trapezoidal Rule.
Author: Scott
"""

def f(x):
    return x**2  # Example: integrate x^2

def trapezoidal(a, b, n):
    h = (b - a) / n
    result = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        result += f(a + i * h)
    return result * h

if __name__ == "__main__":
    a = float(input("Lower bound a (default 0): ") or 0)
    b = float(input("Upper bound b (default 1): ") or 1)
    n = int(input("Number of intervals (default 100): ") or 100)
    print(f"Integral ≈ {trapezoidal(a, b, n):.6f}")
