import time
import numpy as np
from random import *

def pointless_sort(x):
	"""
	This function always returns the same values to show how testing
	works, check out the `test/test_alg.py` file to see.
	"""
	return np.array([1,2,3])

def bubblesort(l):
	"""
	This function sorts the list (L = n) by comparing adjacent
	elements pairwise. It goes through the list (n-1) times.
	"""
	# define counters for assignments & conditionals and timer
	asn = 0
	con = 0
	# starttime = time.monotonic()
	# actual sorting 
	con += 1 # conditional counter
	for passnum in range(0,len(l)-1,1):
		con += 1 # conditional counter
		for i in range(passnum):
			con += 1 # conditional counter
			if l[i]>l[i+1]:
				l[i], l[i+1] = l[i+1], l[i]
				asn += 2 # assignment counter
	# endtime = time.monotonic()
	# dt = endtime - starttime
	return asn, con # get counts for assignments and conditionals

acount = 0
ccount = 0
def quicksort(l, left, right):
	"""
	This function sorts the list (length n) by successively splitting
	the list at an updated pivot point and comparing the two ends to
	each other and the pivot point.
	"""
	# define counters for assignments & conditionals
	global acount
	global ccount
	# starttime = time.monotonic()
	# setting left and right 
	m = left
	n = right
	# actual sorting 
	pivot = l[int((left + right)/2)] # define the pivot point
	while m <= n:
		ccount += 1
		while l[m] < pivot:
			ccount += 1 # conditional counter
			m += 1
			acount += 1 # assignment counter
		while l[n] > pivot:
			ccount += 1 # conditional counter
			n -= 1
			acount += 1 # assignment counter
		# ccount += 1 # conditional counter
		if m <= n:
			l[m], l[n] = l[n], l[m]
			m += 1
			n -= 1
			acount += 4 # assignment counter
	# recursive bit 
	ccount += 1 # conditional counter
	if (left < n):
		quicksort(l, left, n)
	ccount += 1 # conditional counter
	if (m < right):
		quicksort(l, m, right)
	# endtime = time.monotonic()
	# dt = endtime - starttime
	return acount, ccount # get counts for assignments and conditionals

def main(l):
	"""
	This main subroutine runs both sorting algorithms and return the
	results for a vector l.
	"""
	asnb, conb = bubblesort(l)
	asnq, conq = quicksort(l, 0, int(len(l)-1))
	print(l, "\n%s and %s are assignments and conditionals for bubbleSort, respectively.\n" %(asnb, conb))
	print(l, "\n%s and %s are assignments and conditionals for quickSort, respectively.\n" %(asnq, conq))
	return asnb, conb, asnq, conq
