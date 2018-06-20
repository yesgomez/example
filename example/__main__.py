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
		asbu, cobu, asqu, coqu = algs.main(x)
		bcounts.append([asbu, cobu])
		qcounts.append([asqu, coqu])
	return bcounts, qcounts

bdata, qdata = run_stuff()
print ("The results for bubblesort are\n", pd.DataFrame(bdata, index=[np.arange(100,1100,100)], columns=['assignments', 'conditionals']))
print ("The results for quicksort are\n", pd.DataFrame(qdata, index=[np.arange(100,1100,100)], columns=['assignments', 'conditionals']))

def plot_stuff(data, title, comp):
	x = np.arange(100,1100,100)
	y = []
	z = []
	t = []
	for i, ea in enumerate(data): # split the array into x and y values for plotting
		y.append(ea[0])
		z.append(ea[1])
		# t.append(ea[2]*x[i])
	plt.plot(x, y, 'c:', label='assignments') # plot with specified color
	plt.plot(x, z, 'c--', label='conditionals')
	# plt.plot(x, t, 'c', label='time elapsed')
	plt.title(title)
	# adding comparison plot
	if comp is 'n2':
		m = np.arange(100,1100,100) # define n^2
		n = m**2
	elif comp is 'nlogn':
		m = np.arange(100,1100,100) # define nlogn
		n = m * np.log(m) * 10
	else:
		print ("no such line available... yet")
	plt.plot(m, n, 'b', label='expected big O')
	plt.legend()
	plt.show()

plot_stuff(bdata, 'BubbleSort', 'n2')
plot_stuff(qdata, 'QuickSort', 'nlogn')

# Another trivial change