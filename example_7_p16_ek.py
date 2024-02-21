import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 8.5, 1000)
T = 45 + 25*np.exp(-0.056*t)

plt.plot(t, T, '-k')
plt.xlabel("Time (hr)", size=12, weight="bold")
plt.ylabel("Temperature ($\degree$F)", size=12, weight="bold")
plt.xticks(size=12, weight="bold")
plt.yticks(size=12, weight="bold")
plt.xlim([0, 8.5])
plt.ylim([60, 72])
plt.show()
