# this file is only called when the package is called from the command line
import numpy as np
from .algs import quicksort, bubblesort, main

def run_stuff():

    print("This is `run()` from ", __file__)

    x = np.random.rand(100)
    print("Unsorted input: ", x)

    # print("Bubble sort output: ", bubblesort(x))
    # print("Quick sort output: ", quicksort(x))
    print("Unsorted input: ", main(x))

run_stuff()
