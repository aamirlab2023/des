#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Program: first_derivative.py
# Programmer: Aamir Alaud Din, PhD

# Date: 2024.01.17

# Objective(s):
#   To demonstrate the physical meaning of first derivative.

# import required packages
import numpy as np
import matplotlib.pyplot as plt

# define domain and compute the range
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x) + 1.2

# take two points on x-axis and compute corresponding y-axis values
x1 = 2.5
x2 = x1 + 1.0E-6
y1 = np.sin(x1) + 1.2
y2 = np.sin(x2) + 1.2

# print the points (x1, y1) and (x2, y2)
print(f'(x1, y1) = ({x1:.12f}, {y1:.12f})')
print(f'(x2, y2) = ({x2:.12f}, {y2:.12f})')

# compute the slope and print it
m1 = (y2 - y1)/(x2 - x1)
print(f'Slope = m = {m1:.4f}')

# compute and print y-intercept
c1 = y1 - m1*x1 - 1.2
print(f'y-intercept = c = {c1:.4f}\n')

# print the equation of line (tangent to the curve)
xl1 = 1.5
xh1 = 3.5
yl1 = m1*xl1 + c1 + 1.2
yh1 = m1*xh1 + c1 + 1.2

fig = plt.figure(figsize=(14,9))
plt.plot(x, y, '-k')
plt.xticks(size=12, weight='bold')
plt.yticks(size=12, weight='bold')
plt.xlabel('$\\theta$ (Radian)', size=12, weight='bold')
plt.ylabel('sin($\\theta$)', size=12, weight='bold')
plt.show()

ent = input(f'Press enter to plot the first point ({x1:.12f},{y1:.12f})')
fig = plt.figure(figsize=(14,9))
plt.plot(x, y, '-k')
plt.scatter(x1, y1, s=20, c='r')
plt.xticks(size=12, weight='bold')
plt.yticks(size=12, weight='bold')
plt.xlabel('$\\theta$ (Radian)', size=12, weight='bold')
plt.ylabel('sin($\\theta$)', size=12, weight='bold')
plt.show()

ent = input(f'Press enter to plot the second point ({x2:.12f},{y2:.12f})')
fig = plt.figure(figsize=(14,9))
plt.plot(x, y, '-k')
plt.scatter(x1, y1, s=20, c='r')
plt.scatter(x2, y2, s=20, c='g')
plt.xticks(size=12, weight='bold')
plt.yticks(size=12, weight='bold')
plt.xlabel('$\\theta$ (Radian)', size=12, weight='bold')
plt.ylabel('sin($\\theta$)', size=12, weight='bold')
plt.show()

ent = input(f'Press enter to plot the line through the points ({x1:.12f},{y1:.12f}) and ({x2:.12f},{y2:.12f})')
fig = plt.figure(figsize=(14,9))
plt.plot(x, y, '-k')
plt.scatter(x1, y1, s=20, c='r')
plt.scatter(x2, y2, s=20, c='g')
plt.plot([xl1, xh1], [yl1, yh1], '-b')
plt.xticks(size=12, weight='bold')
plt.yticks(size=12, weight='bold')
plt.xlabel('$\\theta$ (Radian)', size=12, weight='bold')
plt.ylabel('sin($\\theta$)', size=12, weight='bold')
plt.show()

# take two points on x-axis and compute corresponding y-axis values
x3 = 5.5
x4 = x3 + 1.0E-6
y3 = np.sin(x3) + 1.2
y4 = np.sin(x4) + 1.2

# compute the slope and print it
m2 = (y4 - y3)/(x4 - x3)

# compute and print y-intercept
c2 = y3 - m2*x3 - 1.2

# print the equation of line (tangent to the curve)
xl2 = 4.5
xh2 = 6.5
yl2 = m2*xl2 + c2 + 1.2
yh2 = m2*xh2 + c2 + 1.2

ent = input(f'Press enter to plot the line through the points ({x3:.12f},{y3:.12f}) and ({x4:.12f},{y4:.12f})')
fig = plt.figure(figsize=(14,9))
plt.plot(x, y, '-k')
plt.scatter(x1, y1, s=20, c='r')
plt.scatter(x2, y2, s=20, c='g')
plt.plot([xl1, xh1], [yl1, yh1], '-b')
plt.scatter(x3, y3, s=20, c='r')
plt.scatter(x4, y4, s=20, c='g')
plt.plot([xl2, xh2], [yl2, yh2], '-b')
plt.xticks(size=12, weight='bold')
plt.yticks(size=12, weight='bold')
plt.xlabel('$\\theta$ (Radian)', size=12, weight='bold')
plt.ylabel('sin($\\theta$)', size=12, weight='bold')
plt.show()
