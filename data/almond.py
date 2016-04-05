import numpy as np
import matplotlib.pyplot as plt


phi = np.linspace(0, 2.0*np.pi, 100)
r = 5.0
b = 4.0
x1 = r*np.cos(phi) + 0.5*b
y1 = r*np.sin(phi)

x2 = r*np.cos(phi) - 0.5*b
y2 = r*np.sin(phi)

x, y = np.meshgrid(np.linspace(-10,10,100), np.linspace(-10,10,100))
z = np.exp(-((x-0.5*b)**2+y**2)**2/5.0**4) * np.exp(-((x+0.5*b)**2+y**2)**2/5.0**4)

fig = plt.figure(figsize=(10, 6), dpi=100)
plt.subplot(121)
plt.plot(x1, y1, '--', linewidth = 2.0, alpha = 1, color = "b")
plt.plot(x2, y2, '--', linewidth = 2.0, alpha = 1, color = "b")
plt.imshow(np.flipud(z), extent = [-10,10, -10,10], cmap = 'Reds')
plt.axis([-8,8,-8,8])
plt.xticks([])
plt.yticks([])
plt.xlabel("x", size = 15)
plt.ylabel("y", size = 15)

plt.subplot(122)
plt.imshow(np.flipud(z), extent = [-10,10, -10,10], cmap = 'Reds')
plt.contour(x, y, z, 10)
plt.axis([-8,8,-8,8])
plt.arrow(1, 0, 4, 0, width = 0.7, head_width=3.0, head_length=2.0, fc='b', ec='b', alpha = 0.3)
plt.arrow(-1, 0, -4, 0, width = 0.7, head_width=3.0, head_length=2.0, fc='b', ec='b', alpha = 0.3)
plt.arrow(0, 1, 0, 2, width = 0.7, head_width=3.0, head_length=2.0, fc='b', ec='b', alpha = 0.3)
plt.arrow(0, -1, 0, -2, width = 0.7, head_width=3.0, head_length=2.0, fc='b', ec='b', alpha = 0.3)
plt.xticks([])
plt.yticks([])
plt.xlabel("x", size = 15)
plt.ylabel("y", size = 15)
plt.savefig("../pics/almond.png", dpi = 100)
