import numpy as np
import timeit
from random import *

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(l):

    # define counters for assignments & conditionals
    asn = 0
    con = 0
    # # conditions for sorting #
    # if len(l) != 0:
    # actual sorting #
    for passnum in range(0,len(l)-1,1):
        for i in range(passnum):
            con += 1 # conditional counter
            if l[i]>l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp
                asn += 1 # assignment counter
    return asn, con # get counts for assignments and conditionals

def quicksort(l):

    left = 0
    right = int(len(l)-1)
    # define counters for assignments & conditionals
    acount = 0
    ccount = 0
    # # conditions for sorting #
    # if len(l) != 0:
    # actual sorting #
    m = left
    n = right
    pivot = l[int((left + right)/2)] # define the pivot point
    while m <= n:
        ccount += 1
        while l[m] < pivot:
            m += 1
            ccount += 1 # conditional counter
        while l[n] > pivot:
            n -= 1
            ccount += 1 # conditional counter
        if m <= n:
            tmp = l[m]
            l[m] = l[n]
            l[n] = tmp
            m += 1
            n -= 1
            acount += 1 # assignment counter
            ccount += 1 # conditional counter
    # recursive bit #
    if left < n:
        quicksort(l, left, n)
    if (m < right):
        quicksort(l, m, right)
    return acount, ccount # get counts for assignments and conditionals

# the main subroutine runs both sorting algorithms and return the results for a vector l #
def main(l):
    asnb, conb = bubblesort(l)
    asnq, conq = quicksort(l)
    print(l, "\n%s and %s are assignments and conditionals for bubbleSort, respectively.\n" %(asnb, conb))
    print(l, "\n%s and %s are assignments and conditionals for quickSort, respectively.\n" %(asnq, conq))
