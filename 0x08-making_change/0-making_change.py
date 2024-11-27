#!/usr/bin/python3
"""
Determines the fewest number of coins
""" 


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to
    meet a given amount total using a greedy algorithm.

    Args:
        coins (list): A list of integers representing the values of coins.
        total (int): The target amount.

    Returns:
        int: The fewest number of coins needed
        to meet the total, or -1 if not possible.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order
    coins.sort(reverse=True)

    count = 0
    for coin in coins:
        if total <= 0:
            break
        # Use as many of this coin as possible
        count += total // coin
        total %= coin

    # If there is any amount left, it means the total cannot be reached
    return count if total == 0 else -1
