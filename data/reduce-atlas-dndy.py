import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

d1 = np.loadtxt("./ATLAS-dNdy.txt").T

eta1 = d1[0]
dNdy1 = np.flipud(d1[3::5])

#
print eta1
dndy_eta = []
for i in range(8):
	dndy_eta.append( interp.interp1d(eta1, dNdy1[i], kind = "cubic") )


eta = np.linspace(-2.65, 2.65, 19)
f = open("pPb-exp.txt", 'w')
for i in range(8):
	y = dndy_eta[i](eta)
	#plt.plot(eta, y, 'o')
	for iy in y:
		f.write("%f "%iy)



cen_L = [0, 1, 5, 10, 20, 30, 40, 60]
cen_H = [1, 5, 10, 20, 30, 40, 60, 90]
color =  [[1,0,0], [0.75, 0.25, 0], [0.5, 0.5, 0], [0.25, 0.75, 0], [0, 1, 0], [0, 0.75, 0.25], [0, 0.5, 0.5], [0, 0, 1]]
print color
fig = plt.figure(figsize=(10, 6), dpi=10)
ax = fig.add_subplot(111)
for i in range(8):
	plt.plot(eta1, dNdy1[i], 'o', color = color[i], label = "%d%% - %d%%"%(cen_L[i], cen_H[i]))
ax.set_xlabel(r"$\eta$", size = 15)
ax.set_ylabel(r"$\mathrm{d}N/\mathrm{d}\eta$", size = 15)
ax.legend(loc='center right')#, bbox_to_anchor=(1, 0.5))
plt.axis([-3, 5, 0, 80])
#ax.semilogy()
#plt.show()
plt.savefig("dNdy-pPb.png", dpi = 100)



