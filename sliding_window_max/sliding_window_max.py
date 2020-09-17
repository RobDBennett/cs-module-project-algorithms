'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
from collections import deque
#Improved Window-

def sliding_window_max(nums, k):
    prods = []
    dq = deque()

    for x in range(len(nums)):
        while dq and dq[-1][0] < nums[x]:
            dq.pop()
        dq.append((nums[x], x))

        if x >= k-1:
            while dq and dq[0][1] < x - k  + 1:
                dq.popleft()
            
            if dq: prods.append(dq[0][0])
    return prods


"""
def sliding_window_max(nums, k):
    prods = []
    if len(nums) >= k:
        for i in range(len(nums) - k + 1):
            prods.append(max(nums[i:i+k]))
           
        return prods
    else:
        return
"""

if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
