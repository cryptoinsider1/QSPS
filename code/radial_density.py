import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.special import genlaguerre

def radial_wavefunction(r, n, l, Z=1):
    a0 = 1.0  # в атомных единицах
    rho = 2 * Z * r / (n * a0)
    L = genlaguerre(n - l - 1, 2*l + 1)(rho)
    norm = (2*Z/(n*a0))**3 * math.factorial(n-l-1) / (2*n*math.factorial(n+l))
    return np.sqrt(norm) * np.exp(-rho/2) * rho**l * L

def radial_density(r, n, l, Z=1):
    R = radial_wavefunction(r, n, l, Z)
    return r**2 * np.abs(R)**2

r = np.linspace(0, 20, 1000)
plt.figure(figsize=(10, 6))

# 1s, 2s, 2p
plt.plot(r, radial_density(r, 1, 0), label='1s', linewidth=2)
plt.plot(r, radial_density(r, 2, 0), label='2s', linewidth=2)
plt.plot(r, radial_density(r, 2, 1), label='2p', linewidth=2)

plt.xlabel('$r$ (в единицах $a_0$)', fontsize=12)
plt.ylabel('$P_{nl}(r)$', fontsize=12)
plt.title('Радиальная плотность вероятности', fontsize=14)
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
