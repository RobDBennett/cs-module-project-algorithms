'''
Input: an integer
Returns: an integer

Monster can eat 1 at a time, 2 at a time, or 3 at a time.
Solution, find total number of ways cookies can be eaten.

This feels like a sorting problem, using recursion to figure out the twist

In the example of 5 cookies...
1- eating 1 at a time 5 times
2- eating 1 than 2 than 2
3- eating 1 than 2 than 1 and 1
4- eating 1 than 1 than 2 than 1
5- eating 1 than 1 than 1 than 2
6- eating 1 than 3 than 1
7- eating 1 than 1 than 3
8- eating 2 than 1 than 1
9- eating 2 than 2 than 1
10- eating 2 than 1 than 2
11- eating 2 than 3
12- eating 3 than 1 than 1
13- eating 3 than 2
So we should have 13 possible solutions for 5 cookies in a jar.

If we treat this like a sorting problem, we can create a number of buckets equal to
the number of cookies + 1
[0] [0] [0] [0] [0] [0]
Then we can do a series of if statements to determine where the cookies initially start.
so cookies 5

Clue to solution was in the readme- https://www.python-course.eu/python3_memoization.php

'''
"""
This gives an error due to the testing file giving a starting memory location.
Rather than editing the test to remove the second argument, I've tried something else below.

def memoize(f):
    memo = {}
    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return helper

def eating_cookies(n):
    if n > 0:
        return eating_cookies(n-3) + eating_cookies(n-2) + eating_cookies(n-1)
    elif n == 0:
        return 1
    else: 
        return 0
"""
#Using the test file as a guide, I've put the memo into the function and eliminated the helper.
def eating_cookies(n, memo=None):
    #Set starting memory-
    if memo == None:
        memo = [0 for i in range(n+1)] #Creates the buckets to store solutions
    if n <= 1: #Check for edge case of 0 cookies or 1, giving 1 way to eat them
        memo[n] = 1
    elif n == 2: #Checks for 2 cookies, giving 2 ways (1+1 or 2)
        memo[n] = 2
    elif memo[n] == 0: #All instances have multiple solutions.
        memo[n] = eating_cookies(n - 1, memo) + eating_cookies(n - 2, memo) + eating_cookies(n - 3, memo)
    return memo[n]

    

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
