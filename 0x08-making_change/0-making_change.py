#!/usr/bin/python3
"""making chages"""


def makeChange(coins, total):
    sortCoin = sorted(coins)[::-1]
    if total == 0 or total < 0:
        return 0
    x = True
    i = 0
    lstCoint = []
    while total != 0 and i != len(sortCoin):
        if total >= sortCoin[i]:
            lstCoint.append(sortCoin[i])
            total -= sortCoin[i]
        else:
            i += 1
    if total != 0:
        return -1
    return len(lstCoint)
