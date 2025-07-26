from fractions import Fraction
import math

def improve_sqrt2_approx(m, n, steps=6):
    approx = Fraction(m, n)
    sqrt2 = math.sqrt(2)

    print(f"{'Step':<5} {'Approximation':<15} {'Decimal':<10} {'Error':<12} {'Direction'}")
    print("-" * 60)

    for i in range(steps):
        decimal = float(approx)
        error = decimal - sqrt2
        direction = "over" if error > 0 else "under"
        print(f"{i:<5} {str(approx):<15} {decimal:<10.6f} {abs(error):<12.6f} {direction}")

        # Apply Hardy's transformation: (m + 2n) / (m + n)
        m_new = approx.numerator + 2 * approx.denominator
        n_new = approx.numerator + approx.denominator
        approx = Fraction(m_new, n_new)

# Example: Start from 1/1 (overestimate)
improve_sqrt2_approx(1, 1, steps=10)
