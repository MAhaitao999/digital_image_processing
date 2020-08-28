"""
Created by HenryMa on 2020/8/28
"""

__author__ = 'HenryMa'


from builtins import *

import cv2
import numpy as np
import matplotlib.pyplot as plt


def homomorphic_filter(image, d0=10, rl=0.5, rh=2, c=4):
    gray = image.copy()
    if len(image.shape) > 2:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = np.float64(gray)
    gray = np.log(gray + 1)  #  防止有元素为0
    rows, cols = gray.shape

    gray_fft = np.fft.fft2(gray)
    gray_fftshift = np.fft.fftshift(gray_fft)
    dst_fftshift = np.zeros_like(gray_fftshift)
    M, N = np.meshgrid(np.arange(-cols//2, cols//2), np.arange(-rows//2, rows//2))
    D = np.sqrt(M ** 2 + N ** 2)
    Z = (rh - rl) * (1 - np.exp(-c * (D ** 2 / d0 ** 2))) + rl
    dst_fftshift = Z * gray_fftshift
    dst_ifftshift = np.fft.ifftshift(dst_fftshift)
    dst_ifft = np.fft.ifft2(dst_ifftshift)
    dst = np.exp(np.abs(dst_ifft)) - 1
    dst = np.uint8(np.clip(dst, 0, 255))

    return dst


if __name__ == '__main__':
    img = cv2.imread('../pic/Fig0462(a)(PET_image).tif', 0)
    plt.subplot(121)
    plt.axis("off")
    plt.imshow(img, cmap='gray')
    plt.subplot(122)
    plt.axis('off')
    plt.imshow(homomorphic_filter(img), cmap="gray")
    plt.show()


