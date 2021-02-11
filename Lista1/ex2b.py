import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import uniform

xPoints = np.arange(start=-3, stop=4)
yPoints = (0, 0.2*(xPoints[1]), 0.2*(xPoints[2]), 0.2*xPoints[3], 0.2*xPoints[4], 0.2*xPoints[5], 0)

fig, ax = plt.subplots(1, 1)
ax.plot(xPoints, yPoints, 'ro', ms=9, mec='r', label='E(X)')
ax.legend(loc='best', frameon=True)
ax.vlines(xPoints, 0, yPoints, colors='r', lw=3)

#plt.plot(xPoints, yPoints)
plt.show()
