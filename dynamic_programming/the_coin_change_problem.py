#!/bin/python3

import math
import os
import random
import re
import sys

'''
Source: HackerRank
Problem:
    You are working at the cash counter at a fun-fair, and you have different types of coins available to you in infinite quantities.
    The value of each coin is already given.
    Can you determine the number of ways of making change for a particular number of units using the given types of coins?
'''
#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#

def getWays(n, c):
    # Write your code here
    # n is the sum unit to make from m coins
    # c is the array with length m c[i] is the denomination

    memoization_table = [0 for i in range(n+1)] 
    memoization_table[0] = 1 # leaf condition

    for denomination in c:
        for i in range(denomination, n+1):
            memoization_table[i] += memoization_table[i-denomination] 
    
    return memoization_table[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')
    
    fptr.close()