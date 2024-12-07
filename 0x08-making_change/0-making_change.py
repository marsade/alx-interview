#!/usr/bin/python3
'''This script determines the fewest number of coins needed to
    make up a given amount.
'''


def makeChange(coins, total):
    '''Calculates the minimum number of coins needed to make
        up the total amount.
    Args: coins: A list of coin denominations.
    total: An integer representing the total amount.
    Returns: An integer representing the minimum number of coins needed.
    '''
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    remaining = total
    for coin in coins:
        while remaining >= coin:
            count += 1
            remaining -= coin
    if remaining == 0:
        return count
    else:
        return -1
