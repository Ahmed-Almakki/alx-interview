#!/usr/bin/python3
"""making chages"""


def making_changes(coins, total, count):
    if total < 0:
        return -1
    if total == 0:
        return 0
    tot = [total - i for i in coins if (total - i) >= 0]
    if len(tot) == 0:
        return -1
    total = min(tot)
    count += making_changes(coins, total, count)
    if count == 0:
        count = -1
    return count


def makeChange(coins, total):
    if total <= 0:
        return 0
    return making_changes(coins, total, count=1)
