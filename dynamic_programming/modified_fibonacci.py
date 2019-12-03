#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the fibonacciModified function below.
def memoize_fibo(fibonacciModified):
    memory = dict()

    def logic(t1, t2, num):
        if num not in memory:          
            memory[num] = fibonacciModified(t1, t2, num) 
        return memory[num] 
  
    return logic

@memoize_fibo
def fibonacciModified(t1, t2, n):

    if n == 1: 
        return t1
    elif n == 2:
        return t2
    else:
        return fibonacciModified(t1, t2, n-2) + pow(fibonacciModified(t1, t2, n-1), 2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t1T2n = input().split()

    t1 = int(t1T2n[0])

    t2 = int(t1T2n[1])

    n = int(t1T2n[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + '\n')

    fptr.close()

