# this file is only called when the package is called from the command line
import numpy as np
import pandas as pd
from example import algs
# from .algs import quicksort, bubblesort, main

def run_stuff():
    print("This is run_stuff() from ", __file__)
    lengths = np.arange(100,1100,100)
    bcounts = []
    qcounts = []
    for le in lengths:
        x = np.random.rand(le)
        print("Unsorted input:\n", x, "\n")
        ab, cb, aq, cq = algs.main(x)
        bcounts.append([ab, cb])
        qcounts.append([aq, cq])
    return bcounts, qcounts

bdata, qdata = run_stuff()
print ("The counts for bubblesort are\n", pd.DataFrame(bdata, index=[np.arange(100,1100,100)], columns=['assignments', 'conditionals']))
print ("The counts for quicksort are\n", pd.DataFrame(qdata, index=[np.arange(100,1100,100)], columns=['assignments', 'conditionals']))

# def plot_stuff():
