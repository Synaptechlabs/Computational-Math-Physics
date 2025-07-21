"""
trig_identity_eval.py
Evaluate common trigonometric identities for a given angle in degrees.
Author: Scott
"""

import math

def evaluate_identities(angle_deg):
    rad = math.radians(angle_deg)
    sin_val = math.sin(rad)
    cos_val = math.cos(rad)
    tan_val = math.tan(rad)
    identity_check = math.isclose(sin_val ** 2 + cos_val ** 2, 1.0, abs_tol=1e-10)
    return sin_val, cos_val, tan_val, identity_check

if __name__ == "__main__":
    try:
        deg = float(input("Enter angle in degrees (default 45): ") or 45)
        sin_v, cos_v, tan_v, identity = evaluate_identities(deg)
        print(f"sin({deg}) = {sin_v:.4f}")
        print(f"cos({deg}) = {cos_v:.4f}")
        print(f"tan({deg}) = {tan_v:.4f}")
        print(f"sin² + cos² ≈ 1? {'Yes' if identity else 'No'}")
    except ValueError:
        print("Invalid input.")
