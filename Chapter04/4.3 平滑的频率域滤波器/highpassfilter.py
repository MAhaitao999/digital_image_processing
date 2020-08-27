"""
Created by HenryMa on 2020/8/27
"""

__author__ = 'HenryMa'


from builtins import *

import cv2
import numpy as np
import matplotlib.pyplot as plt


# 高通滤波器
def HighPassFilter(image, d):
    f = np.fft.fft2(image)
    fshift = np.fft.fftshift(f)

    def make_transform_matrix(d):
        transform_matrix = np.zeros(image.shape)
        center_point = tuple(map(lambda x: int((x-1)/2), image.shape))
        for i in range(transform_matrix.shape[0]):
            for j in range(transform_matrix.shape[1]):
                def cal_distance(pa, pb):
                    from math import sqrt
                    dist = sqrt((pa[0]-pb[0])**2+(pa[1]-pb[1])**2)
                    return dist
                dis = cal_distance(center_point, (i, j))
                if dis <= d:
                    transform_matrix[i, j] = 0
                else:
                    transform_matrix[i, j] = 1
        return transform_matrix
    d_matrix = make_transform_matrix(d)
    new_img = np.abs(np.fft.ifft2(np.fft.ifftshift(fshift*d_matrix)))

    return new_img


if __name__ == '__main__':
    img = cv2.imread('../pic/apple.png', 0)
    plt.subplot(121)
    plt.axis("off")
    plt.imshow(img, cmap='gray')
    plt.subplot(122)
    plt.axis('off')
    plt.imshow(HighPassFilter(img, 70), cmap="gray")
    plt.show()
