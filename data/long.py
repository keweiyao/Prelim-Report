import numpy as np
import matplotlib.pyplot as plt

N = 100
n = np.arange(2*N+1)
L = 30.0 #(2*y_max)
k = 2*np.pi*(n-N)/L
y = 1.0*(n-N)/(2*N)*L
mu = L/2.0
sigma = 3.1
Gamma = 0.4*np.linspace(0,4,5)*sigma**3

plt.figure(figsize = (10, 6), dpi = 10)
plt.subplot(1,2,1)
K = 1.3
eta = np.arcsinh(np.sqrt(K)*np.sinh(y))
print Gamma
for i in range(len(Gamma)):
    gamma = Gamma[i]
    delta = sigma**4*0.5
    Fk = np.exp(1j*mu*k - 0.5 * sigma**2 * k**2 + gamma*1j*k**3 -delta*k**4)/np.sqrt(2*np.pi)*sigma
    J = 1.0/np.sqrt(K)*np.sqrt(K*np.sinh(y)**2+1)/np.cosh(y)
    corr = np.exp(2*np.pi*1j*N*n/(2*N+1))/np.pi/2.0*J
    Fy = np.real(np.multiply(np.fft.fft(Fk), corr))
    plt.plot(eta, np.divide(Fy,Fy[N]/55), '-', label = "$\gamma = %1.1f$"%(gamma/sigma**3))
plt.legend(loc = "upper left")
plt.plot([-15,15],[0,0],'k-')
plt.axis([-15,15,-20,100])
plt.title("w/o regularization", size = 15)
plt.xlabel(r"$\eta$", size = 25)
plt.ylabel(r"$\mathrm{d}N/\mathrm{d\eta}$ (a.u.)", size = 25)

plt.subplot(1,2,2)
K = 1.3
eta = np.arcsinh(np.sqrt(K)*np.sinh(y))
print Gamma
for i in range(len(Gamma)):
    mean = 0.0
    gamma = Gamma[i]
    delta = sigma**4*0.5
    Fk = np.exp(1j*mu*k - 0.5 * sigma**2 * k**2 + gamma*1j*k**3*np.exp(-0.5*sigma**2*(k)**2) - delta*k**4*np.exp(-0.5*sigma**2*(k)**2))/np.sqrt(2*np.pi)*sigma
    J = 1.0/np.sqrt(K)*np.sqrt(K*np.sinh(y)**2+1)/np.cosh(y)
    corr = np.exp(2*np.pi*1j*N*n/(2*N+1))/np.pi/2.0*J
    Fy = np.real(np.multiply(np.fft.fft(Fk), corr))
    plt.plot(eta, np.divide(Fy,Fy[N]/55), '-', label = "$\gamma = %1.1f$"%(gamma/sigma**3))
plt.legend(loc = "upper left")
plt.plot([-20,20],[0,0],'k-')
plt.axis([-15,15,-20,100])
plt.title("w/ regularization", size = 15)
plt.xlabel(r"$\eta$", size = 25)
plt.savefig("../pics/regulate.png", dpi=100)
plt.show()
