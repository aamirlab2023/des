import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi)
cs = [1, 2, 3]
labels = ["c=1", "c=2", "c=3"]
y = np.sin(x)

for i in range(len(cs)):
    plt.plot(x,y+cs[i], label=labels[i])

plt.xlabel("$\\theta$ (Radian)", size=12, weight="bold")
plt.ylabel("sin $\\theta$", size=12, weight="bold")
plt.xticks(size=12, weight="bold")
plt.yticks(size=12, weight="bold")
plt.legend()
plt.show()
