"""
Created by HenryMa on 2020/10/9
"""

__author__ = 'HenryMa'

from builtins import print

import cv2
import numpy as np
import matplotlib.pyplot as plt


theta = np.linspace(0, np.pi, 1000)
print(theta)
rho1 = 2 * np.cos(theta) + np.sin(theta)
rho2 = 2 * np.cos(theta) + 3 * np.sin(theta)
rho3 = 2 * np.cos(theta) + 4 * np.sin(theta)

plt.plot(theta, rho1, 'b', theta, rho2, 'g', theta, rho3, 'r')
plt.show()
