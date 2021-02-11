import matplotlib.pyplot as plt
import numpy as np
from scipy import stats
from scipy.stats import uniform

x = np.linspace(-3, 3, 100)
rv = uniform(-2, 5)

#xk = np.arange(5)
xk = np.arange(start=-3, stop=4)

pk = (0, 0.2*(-xk[1]), 0.2*(-xk[2]), 0.2*xk[3], 0.2*xk[4], 0.2*xk[5], 0)
# pk = (0, 0.2, 0.2, 0.2, 0.2, 0.2, 0)
custm = stats.rv_discrete(name='custm', values=(xk, pk))

fig, ax = plt.subplots(1, 1)
ax.plot(xk, custm.pmf(xk), 'ro', ms=9, mec='r', label='f(X)')
ax.legend(loc='best', frameon=True)
ax.vlines(xk, 0, custm.pmf(xk), colors='r', lw=3)
plt.show()
