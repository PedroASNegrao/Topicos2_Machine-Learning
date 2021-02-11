from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)

x = np.linspace(-2, 2, 100)
rv = uniform(-1, 2)
ex_vec1 = [0, 0.5, 1]

ax.plot(x, rv.cdf(x), 'k-', lw=2, label='CDF')

vals = uniform.ppf(ex_vec1)
np.allclose(ex_vec1, uniform.cdf(vals))

print(vals)

ax.legend(loc='best', frameon=True)
plt.show()
