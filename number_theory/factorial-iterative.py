import sys

def factorial_with_steps(n):
    """
    Compute the factorial of a number using iteration (loop).
    Args:
        n (int): A non-negative integer
    Returns:
        int: Factorial of n (n!)
    """
    steps = []
    result = 1
    for i in range(n, 0, -1):
        steps.append(str(i))
        result *= i
    print(" × ".join(steps))
    return result

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 factorial.py <number>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError("Factorial is undefined for negative numbers.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        sys.exit(1)

    print(f"\n{n}! =")
    result = factorial_with_steps(n)
    print(f"= {result}")
