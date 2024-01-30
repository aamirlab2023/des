import numpy as np

def fp(x):
    return np.cos(x) + np.tan(x) + (3*x**2 - x**3)*np.exp(-x)

def fpp(x):
    return -1*np.sin(x) + (1/(np.cos(x))**2) - (3*x**2 - x**3)*np.exp(-x) + (6*x - 3*x**2)*np.exp(-x)

print(fp(-7.5))
print(fpp(-7.5))
print(fp(7.5))
print(fpp(7.5))
