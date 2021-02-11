from scipy.stats import uniform
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np
fig, ax = plt.subplots(1, 1)

x = np.linspace(-2, 2, 100)
rv = uniform(-1, 2)
rv2 = uniform(-0.2, 0.4)
ex_vec1 = [0, 0.5, 2]


ax.plot(x, rv.pdf(x), 'k-', lw=2, label='PDF(-1,1)')
ax.plot(x, rv2.pdf(x), 'c', lw=2, label='PDF(-0.2,0.2)')

vals = uniform.ppf(ex_vec1)
np.allclose(ex_vec1, uniform.pdf(vals))

print(vals)

ax.legend(loc='best', frameon=True)
plt.show()
