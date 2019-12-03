#!/bin/python3

import math
import os
import random
import re
import sys
# sys.setrecursionlimit(2000)

# Complete the abbreviation function below.
def abbreviation(a, b):
    len_a, len_b = len(a), len(b)
    memory = [[False]*(len_a+1) for _ in range(len_b+1)]
    memory[0][0] = True
    for i in range(len_b+1):
        for j in range(len_a+1):
            if i == 0 and j != 0:
                memory[i][j] = a[j-1].islower() and memory[i][j-1]
            elif i != 0 and j != 0:
                if a[j-1] == b[i-1]:
                    memory[i][j] = memory[i-1][j-1]
                elif a[j-1].upper() == b[i-1]:
                    memory[i][j] = memory[i-1][j-1] or memory[i][j-1]
                elif not (a[j-1].isupper() and b[i-1].isupper()):
                    memory[i][j] = memory[i][j-1]
    return "YES" if memory[len_b][len_a] else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        a = input()

        b = input()

        result = abbreviation(a, b)

        fptr.write(result + '\n')

    fptr.close()

