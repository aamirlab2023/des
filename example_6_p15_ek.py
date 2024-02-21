import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 45181, 1000)
h = (15.00 - 0.000332*t)**2

plt.plot(t, h, '-k')
plt.xlabel("Time (s)", size=12, weight="bold")
plt.ylabel("Height (cm)", size=12, weight="bold")
plt.xticks(size=12, weight="bold")
plt.yticks(size=12, weight="bold")
plt.xlim([0, 55000])
plt.ylim([0, 255])
plt.show()
