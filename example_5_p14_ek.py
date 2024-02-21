import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 50000, 1000)
y = 5000 - 4900*np.exp(-0.01*t)

plt.plot(t, y, '-k')
plt.plot([0, 1000], [5000, 5000], '--b')
plt.xlabel("Time (min)", size=12, weight="bold")
plt.ylabel("Amount of Salt (lb)", size=12, weight="bold")
plt.xticks(size=12, weight="bold")
plt.yticks(size=12, weight="bold")
plt.xlim([0, 1000])
plt.ylim([0, 5500])
plt.show()
