"""
Created by HenryMa on 2020/8/27
"""

__author__ = 'HenryMa'

from builtins import print, int

import cv2
import numpy as np
from matplotlib import pyplot as plt


# shape: 600 * 600
img = cv2.imread('../pic/Fig0438(a)(bld_600by600).tif', 0)
# 返回的是复数 dtype.complex128
fft = np.fft.fft2(img)
print("fft is: ", fft)
# 平移
fftshift = np.fft.fftshift(fft)
print("fftshift is: ", fftshift)
# 频谱 dtype.float64 magnitude_spectrum[180,180] = 329.2611
magnitude_spectrum = 20 * np.log(np.abs(fftshift))
print(magnitude_spectrum[300, 300])

# 如果想要用cv2.imshow()显示
# magnitude_spectrum_uint8 = np.uint8(255 * (magnitude_spectrum / np.max(magnitude_spectrum)))
# cv2.imshow("origin", img)
# cv2.imshow("magnitude_spectrum_uint8", magnitude_spectrum_uint8)
# cv2.waitKey(0)
rows, cols = img.shape
crow, ccol = rows / 2, cols / 2
# 频率中心区域添加60x60的蒙板, 相当于过滤了低频部分
fftshift[int(crow - 30):int(crow+30), int(ccol-30):int(crow+30)] = 0
magnitude_spectrum_filter = 20 * np.log(np.abs(fftshift)+0.0000001)
# 中心平移回到左上角
f_ishift = np.fft.ifftshift(fftshift)
# 使用FFT逆变换, 结果是复数
img_back = np.fft.ifft2(f_ishift)
img_back = np.abs(img_back)
# img_back_uint8 = np.uint8(255 * (img_back / np.max(img_back)))
# cv2.imshow("img_back_uint8", img_back_uint8)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
plt.subplot(221)
plt.imshow(img, cmap='gray')
plt.title('origin image')
# 省略x, y坐标
plt.xticks([]), plt.yticks([])
plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
plt.title('magnitude_spectrum'), plt.xticks([]), plt.yticks([])
plt.subplot(223), plt.imshow(magnitude_spectrum_filter, cmap='gray')
plt.title('High Pass Filter'), plt.xticks([]), plt.yticks([])
plt.subplot(224), plt.imshow(img_back, cmap='gray')
plt.title("High Pass Result"), plt.xticks([]), plt.yticks([])
plt.show()



