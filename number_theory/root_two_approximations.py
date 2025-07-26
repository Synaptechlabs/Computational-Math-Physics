'''
From Hardy Example III. 1. 
'''
approximations = [1.4, 1.41, 1.414, 1.4142]
target = 2

print(f"{'Approx √2':<10} {'Square':<12} {'2 - Square':<12}")
print("-" * 36)

for a in approximations:
    square = a ** 2
    diff = target - square
    print(f"{a:<10} {square:<12.8f} {diff:<12.8f}")
