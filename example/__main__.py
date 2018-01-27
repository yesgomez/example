# this file is only called when the package is called from the command line
import numpy as np
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
print ("The counts for each algorithm are ", bdata, qdata)

# def plot_stuff():
