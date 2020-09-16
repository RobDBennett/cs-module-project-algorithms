'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    mp = {} #Generate hash table.
    for i in range(len(arr)): #Insert all array
        if arr[i] not in mp:
            mp[arr[i]] = 0
        mp[arr[i]] += 1
    for x in mp:
        if (mp[x] == 1):
            return x

    


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")