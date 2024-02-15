import numpy as np
import matplotlib.pyplot as plt

cs = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = np.linspace(-2, 2, 10000)

fig = plt.figure(figsize=(6, 6))

for i in range(len(cs)):
    x = np.arccos((cs[i]-np.exp(y)-y*np.exp(-1*y)-np.exp(-y))/2)
    if cs[i] == 4:
        plt.plot(x, y, '-r', -x, y, '-r')
    else:
        plt.plot(x, y, '-b', -x, y, '-b')
plt.plot([-3.5, 3.5], [0, 0], '-k')
plt.plot([0, 0], [-2.5, 2.5], '-k')
plt.xlabel("x", size=12, weight='bold')
plt.ylabel("y", size=12, weight='bold')
plt.xlim([-3.5, 3.5])
plt.ylim([-2.5, 2.5])
plt.xticks(size=12, weight='bold')
plt.yticks(size=12, weight='bold')
plt.show()
