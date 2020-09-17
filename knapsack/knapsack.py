#!/usr/bin/python
#from gekko import GEKKO
import sys
from collections import namedtuple

Item = namedtuple('Item', ['index', 'size', 'value'])

def knapsack_solver(items, capacity):
    # Your code here
    weight = []
    value = []
    index = []
    kept = []
    for item in items: #Take the items and put them into separate lists.
          dex, wt, v = item
          weight.append(wt)
          value.append(v)
          index.append(dex)
    n = len(items)
    K = [[0 for x in range(capacity + 1)] for x in range(n+1)] #Generate a matrix for value storage.
    for i in range(n + 1):
      for w in range(capacity + 1):
            if i == 0 or w == 0: #Checks starting point
                K[i][w] = 0
            elif weight[i-1] <= w: #Compares the weight, finding 
                  K[i][w] = max(value[i-1] + K[i-1][w - weight[i-1]], K[i-1][w])
            else:
                  K[i][w] = K[i-1][w]
    res = K[n][capacity] #197 for small
    w = capacity
    for i in range(n, 0, -1): #Walk backwards down the range
      if res <= 0: #Added because it gave a few hanging loops
        break
      if res == K[i-1][w]: #Weights are lowering
        continue
      else: #Take the highest value item, save its index to a list, and lower the max value and capacity by appropriate values.
        kept.append(index[i-1]) 
        res = res - value[i-1]
        w = w - weight[i-1]
    kept.sort() #The kept list is backwards since we start with the highest value
    solution = {'Value': K[n][capacity], 'Chosen': kept} #Put this into the format that the test wants.
    return solution


"""
def knapsack_solver(items, capacity):
    item_sizes = []
    item_values = []
    item_index = []
    for x in items: #This can be done easier with a single for loop.
      item_sizes.append(x[1])
    for x in items:
      item_values.append(x[2])
    for x in items:
      item_index.append(x[0])

    n = len(item_sizes)
    W = capacity
    K = [0] * (W + 1)

    for i in range(n+1):
      for w in range(W+1):
        if i == 0 or w == 0:
          K[i][w] = 0
        elif item_sizes[i-1] <= w:
          K[i][w] = max(item_values[i-1] + K[i-1][w-item_sizes[i-1]], K[i-1][w])
        else:
          K[i][w] = K[i-1][w]
    return K[n][W]
"""

"""
    for w in range(1, W + 1):
      max_sub_result = 0
      for i in range(1, n):
        wi = item_sizes[i]
        vi = item_values[i]
        ii = item_index[i]
        if wi <= w:
          subproblem_value = K[w - wi] + vi
          if subproblem_value > max_sub_result:
            max_sub_result = subproblem_value
      K[w] = max_sub_result

    return K[n - 1][W]
  
"""

"""
def total_value(items, capacity):
  return sum([x[2] for x in items]) if sum([x[1] for x in items]) <= capacity else 0

cache= {}

def knapsack_solver(items, capacity):
  
  if not items:
    return ()
  if (items, capacity) not in cache:
    head = items[0]
    tail = items[1:]
    include = (head,) + knapsack_solver(tail, capacity - head[1])
    dont_include = knapsack_solver(tail, capacity)
    if total_value(include, capacity) > total_value(dont_include, capacity):
      answer = include
    else:
      answer = dont_include
    cache[(items, capacity)] = answer
  return cache[(items, capacity)]

def knapsack_solver(items, capacity):
  y = list(items[0])
  v = list(items[2])
  w = list(items[1])
  m = GEKKO()
  x = m.Array(m.Var, len(y), lb=0, ub=1, integer=True)
  m.Obj(-sum(v[i] * x[i] for i in range(len(y))))
  limit = capacity
  m.Equation(sum([w[i]*x[i] for i in range(len(y))]) <= limit)
  m.options.SOLVER = 1
  m.solve()

def knapsack_solver(items, capacity):
  matrix = [[0 for col in range(capacity + 1)] for row in range(len(items[1]))]
  for row in range(len(items[1])):
    for col in range(capacity + 1):
      if items[1][row] > col:
        matrix[row][col] = matrix[row - 1][col]
      else:
        matrix[row][col] = max(matrix[row - 1][col], matrix[row - 1][col - items[1][row]] + items[2][row])
  for i in range(len(items[1])):
    print(matrix[i])
  packed = []
  col = capacity
  for row in range(len(items[1]) - 1, -1, -1):
    if row == 0 and matrix[row][col] != 0:
      packed.insert(0, row)
    if matrix[row][col] != matrix[row - 1][col]:
      packed.insert(0, row)
      col -= items[0][row]
  print(packed)
  print('max value is ', matrix[len(items[1]) -1][capacity])

def knapsack_solver(items, capacity):
    item_sizes = []
    item_values = []
    for x in items:
      item_sizes.append(x[1])
    for x in items:
      item_values.append(x[2])
    n = len(item_sizes)
    W = capacity
    K = [0] * (W + 1)
    for w in range(1, W + 1):
      max_sub_result = 0
      for i in range(1, n):
        wi = item_sizes[i]
        vi = item_values[i]
        if wi <= w:
          subproblem_value = K[w - wi] + vi
          if subproblem_value > max_sub_result:
            max_sub_result = subproblem_value
      K[w] = max_sub_result

    return K[n - 1][W]
"""

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')    