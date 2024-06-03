#!/usr/bin/python3
"""
This module contains the canUnlockAll function.
"""

def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of list of int): A list of lists, where each inner list represents
                                     the keys contained in a box.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    num_boxes = len(boxes)
    unlocked_boxes = [False] * num_boxes
    unlocked_boxes[0] = True
    keys = [0]

    for key in keys:
        for new_key in boxes[key]:
            if new_key not in keys and new_key < num_boxes:
                unlocked_boxes[new_key] = True
                keys.append(new_key)

    return all(unlocked_boxes)
