"""
Created by HenryMa on 2020/8/27
"""

__author__ = 'HenryMa'


from builtins import *

import cv2
import numpy as np
import matplotlib.pyplot as plt


def laplacianFrequencyFilter(image):

    img_arr = np.array(image)

    rows, cols = img_arr.shape

    f = np.fft.fft2(img_arr)
    f_shift = np.fft.fftshift(f)

    H = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            H[i, j] = 1 - 4 * np.math.pi ** 2 * (((i - int(rows / 2)) / rows) ** 2 + ((j - int(cols / 2)) / cols) ** 2)

    img_back = np.fft.ifft2(np.fft.ifftshift(f_shift * H))

    new_img = np.abs(img_back)

    return new_img


if __name__ == '__main__':
    img = cv2.imread('../pic/apple.png', 0)
    plt.subplot(121)
    plt.axis("off")
    plt.imshow(img, cmap='gray')
    plt.subplot(122)
    plt.axis('off')
    plt.imshow(laplacianFrequencyFilter(img), cmap="gray")
    plt.show()
