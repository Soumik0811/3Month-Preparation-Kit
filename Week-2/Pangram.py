import math
import os
import random
import re
import sys
import string

def pangrams(s):
    # Write your code here
    j=set(s.lower().replace(" ",""))  # set function is used to remove duplicate elements
    if len(j)==26:
        return "pangram"
    else:
        return "not pangram"
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
