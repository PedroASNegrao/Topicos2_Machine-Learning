# example of plotting a histogram of a random sample
from matplotlib import pyplot
from numpy.random import normal
# generate a sample
sample = normal(size=10000)
# plot a histogram of the sample
pyplot.hist(sample, bins=20)
pyplot.show()
