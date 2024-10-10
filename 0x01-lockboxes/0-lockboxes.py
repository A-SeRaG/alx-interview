#!/usr/bin/python3
"""
method that determines if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked.

    Args:
        boxes (list of list of int): List of boxes,
        each containing a list of keys.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n  # Keep track of which boxes are unlocked
    unlocked[0] = True  # Box 0 is unlocked by default
    keys = [0]  # Start with the keys from box 0

    while keys:
        current_key = keys.pop()
        for new_key in boxes[current_key]:
            if new_key < n and not unlocked[new_key]:
                unlocked[new_key] = True
                keys.append(new_key)

    return all(unlocked)
