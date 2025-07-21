"""
angle_converter.py
Convert angles between degrees and radians.

Author: Scott
"""

import math

def degrees_to_radians(deg):
    return deg * math.pi / 180.0

def radians_to_degrees(rad):
    return rad * 180.0 / math.pi

if __name__ == "__main__":
    choice = input("Convert (1) degrees to radians or (2) radians to degrees? [1/2]: ").strip()
    if choice == "1":
        deg = float(input("Enter degrees: "))
        print(f"{deg}° = {degrees_to_radians(deg):.6f} radians")
    elif choice == "2":
        rad = float(input("Enter radians: "))
        print(f"{rad} radians = {radians_to_degrees(rad):.6f}°")
    else:
        print("Invalid choice.")
