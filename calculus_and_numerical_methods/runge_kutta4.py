"""
runge_kutta4.py
Solve dy/dx = f(x, y) using 4th-order Runge-Kutta.
Author: Scott
"""

def f(x, y):
    return x + y  # Example ODE

def runge_kutta(x0, y0, x_end, h):
    while x0 < x_end:
        k1 = h * f(x0, y0)
        k2 = h * f(x0 + h/2, y0 + k1/2)
        k3 = h * f(x0 + h/2, y0 + k2/2)
        k4 = h * f(x0 + h, y0 + k3)
        y0 += (k1 + 2*k2 + 2*k3 + k4) / 6
        x0 += h
    return y0

if __name__ == "__main__":
    x0 = float(input("x0 (default 0): ") or 0)
    y0 = float(input("y0 (default 1): ") or 1)
    x_end = float(input("x_end (default 1): ") or 1)
    h = float(input("Step size h (default 0.1): ") or 0.1)
    print(f"Approx y({x_end}) ≈ {runge_kutta(x0, y0, x_end, h):.6f}")
