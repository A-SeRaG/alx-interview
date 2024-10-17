#!/usr/bin/python3
"""
method that calculates the fewest number of operations
needed to result in exactly n H characters in the file
"""


def minOperations(n):
    """
    Minimum Operations method

    Args:
        n: number of operations

    Returns:
        integer & If n is impossible to achieve, return 0
    """
    if n < 2:
        return 0

    operations = 0

    divisor = 2
    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
