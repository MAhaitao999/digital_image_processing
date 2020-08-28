"""
Created by HenryMa on 2020/8/28
https://www.cnblogs.com/lynsyklate/p/8047510.html
"""

__author__ = 'HenryMa'


from builtins import *

import cv2
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats


### 高斯噪声
def GaussianNoisy(image, sigma):
    row, col, ch = image.shape
    mean = 0
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    return noisy.astype('uint8')


### 椒盐噪声
def SaltPepperNoisy(image, s_vs_p=0.5, amount=0.004):
    row, col, ch = image.shape
    out = np.copy(image)
    num_salt = np.ceil(amount * image.size * s_vs_p)
    coords = [np.random.randint(0, i-1, int(num_salt)) for i in image.shape]
    out[coords] = 1
    num_pepper = np.ceil(amount * image.size * (1. - s_vs_p))
    coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in image.shape]
    out[coords] = 0

    return out


### 算术均值滤波

def ArithmeticMeanOperator(roi):
    return np.mean(roi)




if __name__ == '__main__':
    cat = cv2.imread('../pic/cat.jpg')
    cat = cv2.resize(cv2.cvtColor(cat, cv2.COLOR_BGR2RGB), (200, 200))
    plt.subplot(221)
    plt.imshow(cat)
    plt.axis('on')
    plt.subplot(222)
    plt.imshow(GaussianNoisy(cat, 25))
    plt.axis('on')
    plt.subplot(223)
    plt.imshow(SaltPepperNoisy(cat))
    plt.axis('on')
    plt.show()



