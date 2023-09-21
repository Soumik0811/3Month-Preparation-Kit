#Given an array of integers, where all elements but one occur twice, find the unique element.

import math
import os
import random
import re
import sys


def lonelyinteger(a):
    # Write your code here
    
    # With O(n^2)
    # index=0
    # for i in range(len(a)):
    #     c=0
    #     for j in range(len(a)):
    #         if a[i]==a[j]:
    #             c=c+1
    #     if c==1:
    #         index=i
    #         break
    # return a[index]    
    
    # with O(n) complexity: Using the xor operator
    x=0
    for i in a:
        x ^= i
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
