import numpy as np
import matplotlib.pyplot as plt

colors = ['-b', '-g', '-r', '-k', '-y']
c = [5, 4, 3, 2, 1]
xs = []
ys = []
fig = plt.figure(figsize=(6,6))
for i in range(len(c)):
    x = np.linspace(-c[i], c[i], 1000)
    y = np.sqrt(c[i]**2 - x**2)
    xs.append(x)
    ys.append(y)
    plt.plot(x, y, colors[i], x, -y, colors[i])
plt.plot([-6, 6], [0, 0], '-k')
plt.plot([0, 0], [-6, 6], '-k')
plt.scatter(4, -3, c="r", s=20)
plt.text(4.25, -3.25, "(4, -3)", size=12, weight="bold")
plt.xlabel("x", size=12, weight="bold")
plt.ylabel("y", size=12, weight="bold")
plt.xticks(size=12, weight="bold")
plt.yticks(size=12, weight="bold")
plt.show()

"""
x = np.linspace(-5, 5, 1000)
c = 5
yu = np.sqrt(c**2 - x**2)
yl = -1*yu
print(len(x))
print(len(yu))

fig = plt.figure(figsize=(5,5))
plt.plot(x, yu, '-b', x, yl, '-b')
plt.show()
"""
