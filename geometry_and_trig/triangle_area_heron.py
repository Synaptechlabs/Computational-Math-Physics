"""
triangle_area_heron.py
Calculate the area of a triangle using Heron's formula.
Author: Scott
"""

import math

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

if __name__ == "__main__":
    try:
        a = float(input("Enter side a (default 3): ") or 3)
        b = float(input("Enter side b (default 4): ") or 4)
        c = float(input("Enter side c (default 5): ") or 5)
        area = triangle_area(a, b, c)
        print(f"Triangle area ≈ {area:.4f} square units")
    except ValueError:
        print("Invalid input.")
