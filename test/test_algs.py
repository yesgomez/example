import numpy as np
from example import algs

def test_pointless_sort():
    # generate a new random vector of length 100
    x = np.random.rand(100)
    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

# generic tests for algorithm logic #
# def test_bubblesort():
#     # generate random vector of length 100
#     x = np.random.rand(100)
#     algs.bubblesort(x)
#
# def test_quicksort():
#     # generate random vector of length 100
#     x = np.random.rand(100)
#     algs.quicksort(x, 0, int(len(x)-1))
#
# def test_main():
#     # generate random vector of length 100
#     x = np.random.rand(100)
#     algs.main(x)

# testing specific edge cases #
def test_empty():
    # generate random vector of length 0
    x = np.empty([1,1])
    algs.main(x) # check if it fails if the vector is empty

def test_single():
    # generate random vector containing 1 element
    x = np.random.rand(1,1)
    algs.main(x)

def test_duplicated():
    # generate random vector containing 100 elements
    x = np.random.rand(1, 100)
    y = x.tolist()
    print (len(y))
    z = y[0]
    # add the first element to the list again (duplicate it)
    y.append(z)
    algs.main(y)

def odd_even():
    # generate random vector containing 99 elements
    x = np.random.rand(1, 99)
    algs.main(x)
    # generate random vector containing 999 elements
    x = np.random.rand(1, 999)
    algs.main(x)
