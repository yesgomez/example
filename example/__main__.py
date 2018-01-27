# this file is only called when the package is called from the command line
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from example import algs

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

def plot_stuff(data, color, title, comp):
    x = []
    y = []
    for ea in data: # split the array into x and y values for plotting
        x.append(ea[0])
        y.append(ea[1])
    plt.plot(x, y, color) # plot with specified color
    plt.title(title)
    # adding comparison plot
    if comp = 'n2':
        m = np.arange(0,x[-1],1) # define n^2
        n = m**2
    elif comp = 'nlogn':
        m = np.arange(0,x[-1],1) # define nlogn
        n = m * np.log(m)
    else:
        print "no such line available... yet"
    plt.plot(m, n, '--')
    plt.show()

plot_stuff(bdata, 'r', 'BubbleSort', 'n2')
plot_stuff(qdata, 'b', 'QuickSort', 'nlogn')
