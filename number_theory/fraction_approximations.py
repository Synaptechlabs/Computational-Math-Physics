'''
From Hardy Example III. 2. 
'''

from fractions import Fraction

fractions = [
    Fraction(1, 1),
    Fraction(3, 2),
    Fraction(7, 5),
    Fraction(17, 12),
    Fraction(41, 29),
    Fraction(99, 70)
]

print(f"{'Approx √2':<10} {'Square':<20} {'2 - Square':<20}")
print("-" * 55)

for frac in fractions:
    square = frac ** 2
    diff = Fraction(2) - square
    print(f"{str(frac):<10} {str(square):<20} {str(diff):<20}")
