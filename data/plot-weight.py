import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp


PbPb = np.loadtxt("weight-PbPb.txt")
pPb = np.loadtxt("weight-pPb.txt")
n = np.arange(1, len(pPb)+1)
print n

fig = plt.figure(figsize=(10, 6), dpi=10)
ax = fig.add_subplot(111)
plt.plot(n, PbPb, 'ro-', label = "Pb + Pb")
plt.plot(n, pPb, 'bo-', label = "p + Pb")

ax.set_xlabel(r"$n$", size = 15)
ax.set_ylabel(r"$\sum_{i=1}^{n}w_i / \sum_{i=1}^{N}w_i$", size = 15)
plt.plot([5.5, 5.5], [0, 2], 'g--', linewidth = '2')
ax.legend(loc='center right')
plt.axis([0, 8, 0.7, 1.1])
#plt.show()
plt.savefig("../pics/weight.png", dpi = 100)



