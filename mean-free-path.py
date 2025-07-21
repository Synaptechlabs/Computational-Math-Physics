# ------------------------------------------------------------------------------
# Estimate of Mean Free Path for Air Molecules at STP
#
# Author: Scott K. Douglass
# Date: 2025-07-20
# Description:
#     Computes the mean free path of air molecules at standard temperature
#     and pressure (STP) using classical kinetic theory:
#
#         λ = 1 / (√2 * π * d² * n)
#
#     where:
#         d = molecular diameter (approx. 3.7 × 10⁻¹⁰ m)
#         n = number density of air molecules (~2.7 × 10²⁵ m⁻³)
#
# Dependencies: math
# ------------------------------------------------------------------------------


import math

# Default values
DEFAULT_DIAMETER = 3.7e-10  # meters
DEFAULT_DENSITY = 2.7e25    # particles per m³

# Prompt user for input (or use defaults)
try:
    d_input = input(f"Enter molecular diameter in meters [default: {DEFAULT_DIAMETER:.2e}]: ").strip()
    d = float(d_input) if d_input else DEFAULT_DIAMETER

    n_input = input(f"Enter number density in m⁻³ [default: {DEFAULT_DENSITY:.2e}]: ").strip()
    n = float(n_input) if n_input else DEFAULT_DENSITY

    lambda_mfp = 1 / (math.sqrt(2) * math.pi * d**2 * n)

    print(f"\nEstimated mean free path ≈ {lambda_mfp:.2e} meters")

except ValueError:
    print("Invalid input. Please enter valid numbers or press Enter for default.")