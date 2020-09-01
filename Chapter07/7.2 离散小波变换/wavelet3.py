"""
Created by HenryMa on 2020/9/1
"""

__author__ = 'HenryMa'

from builtins import *

import numpy as np
import pywt
import cv2
import matplotlib.pyplot as plt


img = cv2.imread('../pic/cat.png')
img = cv2.resize(img, (448, 448))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY).astype(np.float32)

plt.figure('二维图像多级分解')
coeffs = pywt.wavedec2(img, 'haar', level=2)
cA2, (cH2, cV2, cD2), (cH1, cV1, cD1) = coeffs

# 将每个子图的像素范围都归一化到与CA2一致  CA2 [0,255* 2**level]
AH2 = np.concatenate([cA2, cH2+510], axis=1)
VD2 = np.concatenate([cV2+510, cD2+510], axis=1)
cA1 = np.concatenate([AH2, VD2], axis=0)

AH = np.concatenate([cA1, (cH1+255)*2], axis=1)
VD = np.concatenate([(cV1+255)*2, (cD1+255)*2], axis=1)
img = np.concatenate([AH, VD], axis=0)

plt.imshow(img, 'gray')
plt.title('2D WT')
plt.show()
