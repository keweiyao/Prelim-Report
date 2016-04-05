import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp
m = np.loadtxt("out.txt").T[3]
B = np.loadtxt("out.txt").T[1]
m = np.sort(m)[::-1]
B = np.sort(B)

cen = np.array([5, 10, 20, 30, 40, 50, 60, 70, 80, 90])*1000


ba = B[cen]

fig = plt.figure(figsize = (10,6), dpi = 10)
plt.subplot(2,1,1)
plt.xticks([])
plt.yticks([])
x, y = np.meshgrid(np.linspace(-10,10,50), np.linspace(-10,10,50))
i = -1
b = 0
z = np.exp(-((x-0.5*b)**2+y**2)**2/7.0**4) * np.exp(-((x+0.5*b)**2+y**2)**2/7.0**4)
plt.imshow(z, extent = [90, 1000, 0, 10], vmax = 1, cmap = 'Reds')
for b in ba[::-1]:
	i += 1
	z = np.exp(-((x-0.5*b)**2+y**2)**2/7.0**4) * np.exp(-((x+0.5*b)**2+y**2)**2/7.0**4)
	plt.imshow(z, extent = [i*10, (i+1)*10, 0, 10], vmax = 1, cmap = 'Reds')
plt.axis([0, 100, 0, 10])
plt.xlim([0, 100])

plt.subplot(2,1,2)
H, xx, v = plt.hist(m, 1000, histtype='step', color = 'r')
xm = 0.5*(xx[0:len(xx)-1]+xx[1:])
f = interp.interp1d(xm, H)
cut = m[cen]
for c in cut:
	plt.plot([c, c], [1, f(c)], 'r--', linewidth = 1.5, alpha = 0.5)
plt.semilogy()
plt.axis([0,200, 1, 10000])
plt.xlabel("Multiplicity (a.u.)" , size = 15)
plt.ylabel("Counts" , size = 15)

plt.subplots_adjust(hspace=0)
plt.savefig("../pics/centrality.png", dpi = 100)
plt.show()


