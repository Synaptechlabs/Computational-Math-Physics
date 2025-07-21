"""
circle_area_circumference.py
Compute the area and circumference of a circle.
Author: Scott
"""

import math

def circle_metrics(radius):
    area = math.pi * radius ** 2
    circumference = 2 * math.pi * radius
    return area, circumference

if __name__ == "__main__":
    try:
        r = float(input("Enter radius (default 1.0): ") or 1.0)
        area, circ = circle_metrics(r)
        print(f"Area ≈ {area:.4f}")
        print(f"Circumference ≈ {circ:.4f}")
    except ValueError:
        print("Invalid input.")
