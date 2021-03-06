from scipy.stats import uniform
import matplotlib.pyplot as plt
import numpy as np
fig, ax = plt.subplots(1, 1)

x = np.linspace(-2, 2, 100)
rv = uniform(-1, 2)
ex_vec1 = [0.001, 0.5, 0.999]

ax.plot(x, rv.pdf(x), 'k-', lw=2, label='PDF')
#ax.plot(x, rv.custm.pmf(x), 'k-', lw=2, label='PDF')


vals = uniform.ppf(ex_vec1)
np.allclose(ex_vec1, uniform.cdf(vals))

print(vals)

ax.legend(loc='best', frameon=True)
plt.show()
