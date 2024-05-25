# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 15:23:23 2022

@author: Venom
"""
import matplotlib.pyplot as plt
import scipy.optimize as optimize
import numpy as np

# data
F1 = np.array([532, 522, 512, 502, 492, 482, 472, 462, 452, 442, 432, 422, 412, 402, 392, 382, 372, 362, 352, 342, 332, 322, 312, 302, 292, 282, 272])
t1 = np.array([412, 452, 427, 433, 391, 421, 445, 418, 398, 418, 393, 395, 412, 379, 401, 411, 411, 407, 397, 404, 397, 390, 424, 390, 388, 413, 419])

plt.plot(t1, F1, 'ro', label="original data")

# curvefit

# def func(t, a, b):
#     return a + b * np.log(t)
def f(x, p1, p2, p3):
    return p3*(p1/((x-p2)**2 + (p1/2)**2))

popt, pcov = optimize.curve_fit(f, t1, F1, p0=[1,0,1] , bounds=(35,45) )#maxfev=1000  
t = np.linspace(50, 3600 * 24 * 28, 13)
plt.plot(t, f(t, *popt), label="Fitted Curve")
plt.legend(loc='upper left')
plt.show()