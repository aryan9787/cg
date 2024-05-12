import numpy as np
import matplotlib.pyplot as plt
import scipy as scipy

def bezier_curve(points, t):
    n = len(points)
    B = np.zeros(2)
    for i in range(n):
        B += scipy.special.comb(n-1, i) * ((1-t)**(n-1-i)) * (t**i) * points[i]
    return B

points = np.array([[0, 0], [0, 1], [1, 1], [1, 0]])

t = np.linspace(0, 1, num=1000)
curve = np.array([bezier_curve(points, i) for i in t])

plt.plot(curve[:, 0], curve[:, 1])
plt.show()