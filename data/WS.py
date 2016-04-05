import numpy as np
import matplotlib.pyplot as plt

def WS(R):
	return 1.0/(1.0 + np.exp(2.0*(np.abs(R)-5.0)))
def GM(a, b, p):
	if np.abs(p)>0.01:
		return (0.5*(a**p + b**p))**(1.0/p)
	else:
		return np.sqrt(a*b)
x = np.linspace(-8,8.0,100)
y = WS(x)


r = np.random.rand(1500*3).reshape([1500,3])*16.0-8.0
rnew = []
for r1 in r:
	R = np.sqrt(r1[0]**2 + r1[1]**2 + r1[2]**2)
	ws = WS(R)
	if ws > np.random.rand():
		rnew.append(r1)
rnew = np.array(rnew).T

r = np.random.rand(1500*3).reshape([1500,3])*16.0-8.0
rnew2 = []
for r1 in r:
	R = np.sqrt(r1[0]**2 + r1[1]**2 + r1[2]**2)
	ws = WS(R)
	if ws > np.random.rand():
		rnew2.append(r1)
rnew2 = np.array(rnew2).T

phi = np.linspace(0, 2*np.pi, 100)
r = 5.0
y = r*np.cos(phi) * (1.0+0.4*np.sin(phi)**2)
x = r*np.sin(phi) * (0.5)

plt.figure(figsize=(10,6), dpi = 10)
plt.plot(x, y, "r--", linewidth = 4.0, alpha = 1.0)
#plt.subplot(1,2,1)
#plt.scatter(rnew[0], rnew[1],s=400.0, c=(rnew[2]+8)/16, alpha=0.5)
#plt.axis([-8,8,-8,8])
plt.xlabel("x/fm", size = 25)
plt.ylabel("y/fm", size = 25)
#plt.plot(x, y*5)

plt.subplot(1,1,1)
c = (rnew[2]+8)/16.
plt.scatter(rnew[0]+3, rnew[1],s=400.0, c=np.array([c*0.0, c*1.0, c*0.0]).T, linewidths=0.2, alpha=0.3)
plt.scatter(rnew2[0]-3, rnew2[1],s=400.0, c=np.array([c*0.0, c*0.0, c*1.0]).T, linewidths=0.2, alpha=0.3)
plt.axis([-12, 12, -8,8])
plt.xticks([-12, -8, -4, 0, 4, 8, 12], size = 15)
plt.yticks([-8, -4, 0, 4, 8], size = 15)
plt.savefig("../pics/nuclei.png")
plt.show()

"""
Ta = np.linspace(0,4.0,100)
Tb = np.linspace(0,4.0,100)

TA, TB = np.meshgrid(Ta, Tb)

p = [-1, -0.3, 0.0, 1.0]
for i in range(4):
	TR = GM(TA, TB, p[i])
	plt.subplot(2,2,i+1)
	plt.imshow(np.flipud(TR), alpha = 0.5, extent = [0,4,0,4])
	plt.colorbar()
	plt.contour(TR, extent = [0,4,0,4])
	plt.title("p = %1.1f"%(p[i]))
	plt.xticks([0,1,2,3,4])
	plt.yticks([0,1,2,3,4])
	if i==0 or i==2:
		plt.ylabel(r"$T_A$")
	if i==2 or i==3:
		plt.xlabel(r"$T_B$")
plt.show()
"""
