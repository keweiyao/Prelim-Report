import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as interp

d1 = np.loadtxt("./ALICE-dNdy-1.txt").T
d2 = np.loadtxt("./ALICE-dNdy-2.txt").T

eta1 = 0.5*(d1[0] + d1[1])
dNdy1 = d1[2::2]

eta2 = d2[0]
dNdy2 = d2[3::5]


a = -(eta2[len(eta2)-6:len(eta2)])[::-1]
b = np.fliplr(dNdy2[:, len(eta2)-6:len(eta2)])

eta2 = np.concatenate((a, eta2))
print eta2
dNdy2 = np.concatenate((b, dNdy2), axis = 1)

cen_L = [0, 5, 10, 20, 30, 40, 50, 60, 70, 80]
cen_H = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90]
color =  [[1,0,0], [0.75, 0.25, 0], [0.5, 0.5, 0], [0.25, 0.75, 0], [0, 1, 0], [0, 0.75, 0.25], [0, 0.5, 0.5], [0, 0.25, 0.75], [0, 0, 1], [0.5, 0, 0.5]]
print color
fig = plt.figure(figsize=(10, 6), dpi=10)
ax = fig.add_subplot(111)
for i in range(4):
	print i
	plt.plot(eta1, dNdy1[i], 'o', color = color[i], label = "%d%% - %d%%"%(cen_L[i], cen_H[i]))
for i in range(6):
	print i+4
	plt.plot(eta2, dNdy2[i], 'o', color = color[i+4], label = "%d%% - %d%%"%(cen_L[i+4], cen_H[i+4]))
#box = ax.get_position()
#ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])
ax.set_xlabel(r"$\eta$", size = 15)
ax.set_ylabel(r"$\mathrm{d}N/\mathrm{d}\eta$", size = 15)
ax.legend(loc='center right')#, bbox_to_anchor=(1, 0.5))
plt.axis([-6, 10, 10, 3000])
ax.semilogy()
#plt.show()


#
dndy_eta = []
for i in range(4):
	dndy_eta.append( interp.interp1d(eta1, dNdy1[i], kind = "cubic") )
for i in range(6):
	dndy_eta.append( interp.interp1d(eta2, dNdy2[i], kind = "cubic") )


eta = np.linspace(-4.875, 4.875, 19)
f = open("PbPb-exp.txt", 'w')
for i in range(10):
	y = dndy_eta[i](eta)
	#plt.plot(eta, y, 'o')
	for iy in y:
		f.write("%f "%iy)
#plt.show()
plt.savefig("../pics/dNdy-PbPb.png", dpi = 100)



