import os


def fibonacci(n):
    """Compute the nth number in the Fibonacci sequence."""
    x = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
