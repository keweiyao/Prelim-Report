import numpy as np
import matplotlib.pyplot as plt

b = np.linspace(0, 3.0, 100)
a = 9.0
w = 0.5
P = (1.0 - np.exp(-a/4.0/np.pi/w**2*np.exp(-b**2/4.0/w**2)))
plt.figure(figsize = (10, 6), dpi = 10)
plt.plot(b, P, "r-", linewidth = 2.0)
plt.xticks([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], size = 15)
plt.yticks([0, 0.5, 1.0], size = 15)
plt.xlabel(r"$b/\mathrm{fm}$", size = 20)
plt.ylabel(r"$P_\mathrm{coll}$", size = 20)
plt.savefig("../pics/Pcoll.png", dpi = 100)
plt.show()
