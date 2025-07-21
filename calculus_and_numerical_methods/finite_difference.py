"""
finite_difference.py
Compute finite difference approximation of the first derivative.
Author: Scott
"""

def finite_difference(f, x, h=1e-5):
    return (f(x + h) - f(x)) / h

if __name__ == "__main__":
    f = lambda x: x**2  # Example function
    x = float(input("Enter x (default 2.0): ") or 2.0)
    print(f"f'(x) ≈ {finite_difference(f, x):.5f}")
