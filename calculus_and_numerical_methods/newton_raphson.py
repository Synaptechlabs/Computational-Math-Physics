"""
newton_raphson.py
Root-finding using the Newton-Raphson method.
Author: Scott
"""

def f(x):
    return x**2 - 2  # Example: root of x^2 - 2 = 0

def df(x):
    return 2 * x  # Derivative

def newton_raphson(x0, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fx = f(x0)
        dfx = df(x0)
        if dfx == 0:
            raise ZeroDivisionError("Derivative is zero.")
        x1 = x0 - fx / dfx
        if abs(x1 - x0) < tol:
            return x1
        x0 = x1
    raise Exception("Max iterations exceeded")

if __name__ == "__main__":
    x0 = float(input("Initial guess (default 1.0): ") or 1.0)
    root = newton_raphson(x0)
    print(f"Root ≈ {root:.6f}")
