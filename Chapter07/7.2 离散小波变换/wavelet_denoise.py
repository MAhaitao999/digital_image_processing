"""
Created by HenryMa on 2020/9/1
"""

__author__ = 'HenryMa'

from builtins import *

import pywt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math


# data = np.linspace(1, 10, 10)
# print(data)
#
# data_soft = pywt.threshold(data=data, value=6, mode='soft', substitute=12)
# print(data_soft)
#
# data_hard = pywt.threshold(data=data, value=6, mode='hard', substitute=12)
# print(data_hard)
#
# data_greater = pywt.threshold(data, 6, 'greater', 12)
# print(data_greater)
#
# data_less = pywt.threshold(data, 6, 'less', 12)
# print(data_less)

# Get data:
ecg = pywt.data.ecg()
# print(ecg)
index = []
data = []
for i in range(len(ecg)-1):
    X = float(i)
    Y = float(ecg[i])
    index.append(X)
    data.append(Y)

# print(index)
# print(data)

# Create wavelet object and define parameters
w = pywt.Wavelet('db8')
maxlev = pywt.dwt_max_level(len(data), w.dec_len)
# print('maximum level is: ' + str(maxlev))
threshold = 0.04  # Threshold for filtering

# Decompose into wavelet components, to the level selected:
coeffs = pywt.wavedec(data, 'db8', level=maxlev)
print(coeffs)

for i in range(1, len(coeffs)):
    coeffs[i] = pywt.threshold(coeffs[i], threshold*max(coeffs[i]))  # 将噪声滤波

datarec = pywt.waverec(coeffs, 'db8')  # 将信号进行小波重构

mintime = 0
maxtime = mintime + len(data) + 1

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(index[mintime:maxtime], data[mintime:maxtime])
plt.xlabel('time (s)')
plt.ylabel('microvolts (uV)')
plt.title("Raw signal")
plt.subplot(2, 1, 2)
plt.plot(index[mintime:maxtime], datarec[mintime:maxtime-1])
plt.xlabel('time (s)')
plt.ylabel('microvolts (uV)')
plt.title("De-noised signal using wavelet techniques")

plt.tight_layout()
plt.show()


