#!/usr/bin/python

import sys

def making_change(amount, denominations):
  ways = [1]+[0]*amount
  for coin in denominations:
    for i in range(coin,amount+1):
      ways[i] += ways[i-coin]
  return ways[amount]

"""
from functools import lru_cache

@lru_cache(maxsize= None)
def making_change(amount, denominations):
  if amount < 0:
    return 0
  if amount == 0:
    return 1
  else:
    return sum(making_change(amount-coin) for coin in denominations)
"""

if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")