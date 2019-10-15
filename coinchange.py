#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
###### Code #####
def getWays(amounts, coins):
    combinations = [0 for x in range(amounts+1)]
    combinations[0]=1
    for coin in coins:
        for amount in range(1,amounts+1):
            if amount>=coin:
                combinations[amount]+=combinations[amount-coin]
    return combinations[amounts]
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    amounts = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    coins = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(amounts, coins)

    fptr.write(str(ways) + '\n')

    fptr.close()
