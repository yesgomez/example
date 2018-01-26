# this file is only called when the package is called from the command line
import numpy as np
from .algs import quicksort, bubblesort

def run_stuff():
    """
    This function is called in `__main__.py`
    """
    print("This is `run()` from ", __file__)

    x = np.random.rand(10)
    print("Unsorted input: ", x)

    print("Bubble sort output: ", bubblesort(x))
    print("Quick sort output: ", quicksort(x))

run_stuff()
