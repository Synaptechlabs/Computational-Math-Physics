"""
taylor_series.py
Compute Taylor series approximation for exp(x), sin(x), cos(x).
Author: Scott
"""

import math

def taylor_exp(x, n=10):
    return sum((x**i)/math.factorial(i) for i in range(n))

def taylor_sin(x, n=10):
    return sum(((-1)**i)*(x**(2*i+1))/math.factorial(2*i+1) for i in range(n))

def taylor_cos(x, n=10):
    return sum(((-1)**i)*(x**(2*i))/math.factorial(2*i) for i in range(n))

if __name__ == "__main__":
    x = float(input("Enter x (default 1.0): ") or 1.0)
    terms = int(input("Number of terms (default 10): ") or 10)
    print(f"exp({x}) ≈ {taylor_exp(x, terms):.6f}")
    print(f"sin({x}) ≈ {taylor_sin(x, terms):.6f}")
    print(f"cos({x}) ≈ {taylor_cos(x, terms):.6f}")
