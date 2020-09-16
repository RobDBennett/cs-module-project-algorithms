#!/usr/bin/python

import sys

#A similar problem to the cookie monster thing, just with strings instead of numbers.

def combos(n, currentList):
  choices = ["rock", "paper", "scissors"]
  if len(currentList) == 0:
    return [[]] if n < 1 else combos(n-1, [[c] for c in choices])

  if n < 1:
    return currentList
  
  newList= []
  for combo in currentList:
    for choice in choices:
      newCombo = combo.copy()
      newCombo.append(choice)
      newList.append(newCombo)
  return combos(n-1, newList)

def rock_paper_scissors(n):
  return combos(n, [])


"""
def rock_paper_scissors(n, options=("rock", "paper", "scissors")):
  
  if n == 0: #Test specific response.
    return [[]]
  out = []
  for i in range(0, len(options)):
    m = options[i]
    rem = options[i+1:]
  
  for p in rock_paper_scissors(n-1, rem):
    out.append([m]+p)
  return out
"""
if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')