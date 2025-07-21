"""
trig_table_generator.py
Generate a sine, cosine, and tangent table from 0° to 360° in steps.

Author: Scott
"""

import math

def degrees_to_radians(deg):
    pi = 3.141592653589793
    return deg * (pi / 180)

def generate_table(step=1):
    print(f"{'Angle (°)':>10} | {'sin(θ)':>10} | {'cos(θ)':>10} | {'tan(θ)':>10}")
    print("-" * 44)
    for deg in range(0, 361, step):
        rad = degrees_to_radians(deg)
        sin_val = math.sin(rad)
        cos_val = math.cos(rad)
        tan_val = math.tan(rad) if abs(math.cos(rad)) > 1e-10 else float('inf')
        print(f"{deg:10} | {sin_val:10.4f} | {cos_val:10.4f} | {tan_val:10.4f}")

if __name__ == "__main__":
    generate_table()
