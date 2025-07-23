import sys

fact=[]

def write_fact():
    expr = " × ".join(str(x) for x in reversed(fact))
    return expr

def factorial(n):
    """
    Compute the factorial of a number using recursion.
    Args:
        n (int): A non-negative integer
    Returns:
        int: Factorial of n (n!)
    """
    if n==1:
        fact.append(1)
        return 1
    else:
        fact.append(n)
        return factorial(n-1)*n
    return n

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python factorial.py <number>")
        sys.exit(1)
    
    try:
        n = int(sys.argv[1])
        if n < 0:
            raise ValueError
    except ValueError:
        print("Please provide a non-negative integer.")
        sys.exit(1)

    result = factorial(n)
    expression = write_fact()
    print(f"{n}! = {expression} = {result}")