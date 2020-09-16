'''
Input: a List of integers
Returns: a List of integers
'''
"""
First attempt. Not difficult with numpy.
import numpy as np

def product_of_all_other_numbers(arr):
    prods = []
    for i in range(len(arr)):
        temp = arr
        x = temp[i]
        temp[i] = 1
        prods.append(np.prod(temp))
        temp[i] = x
    return prods
"""
def product_of_all_other_numbers(arr):
    if len(arr) == 2:
        return [arr[1], arr[0]] #Arranged to match test.
    if len(arr) <=1:
        return arr
    
    products = [0 for x in arr] #Creates buckets of 0's
    p = 1
    for i in range(len(arr)): #'Walks' down list populating with products
        products[i] = p
        p *= arr[i]
    
    p = 1
    for i in range(len(arr) -1, -1, -1): #Start/Stop/Step
        products[i] *= p #'Walks' up list to repopulate.
        p *= arr[i]

    return products

if __name__ == '__main__':
    # Use the main function to test your implementation
    #arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
