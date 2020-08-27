"""
Created by HenryMa on 2020/8/27
"""

__author__ = 'HenryMa'

from builtins import print, int

import cv2
import numpy as np


img = cv2.imread('../pic/Fig0438(a)(bld_600by600).tif', 0)
dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
# 平移还是要靠numpy
dft_shift = np.fft.fftshift(dft)
magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))
# float32
print(dft.dtype)

rows, cols = img.shape
crow, ccol = int(rows / 2), int(cols / 2)

# 创建蒙板
mask = np.ones((rows, cols, 2), np.uint8)
msize = 70
mask[crow-int(msize/2): crow+int(msize/2), ccol-int(msize/2): ccol+int(msize/2)] = 0
fshift = dft_shift * mask
f_ishift = np.fft.ifftshift(fshift)

# 此时img_back为复数
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

cv2.imshow('origin', img)
cv2.imshow('img_back', img_back)
cv2.waitKey(0)
cv2.destroyAllWindows()

