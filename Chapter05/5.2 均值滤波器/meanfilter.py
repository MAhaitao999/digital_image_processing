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
    return noisy.astype(np.uint8)


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


def ArithmeticMeanAlgorithm(image):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            new_image[i-1, j-1] = ArithmeticMeanOperator(image[i-1: i+2, j-1: j+2])

    new_image = (new_image - np.min(image)) * (255 / np.max(image))

    return new_image.astype(np.uint8)


def rgbArithmeticMean(image):
    r, g, b = cv2.split(image)
    r = ArithmeticMeanAlgorithm(r)
    g = ArithmeticMeanAlgorithm(g)
    b = ArithmeticMeanAlgorithm(b)

    return cv2.merge([r, g, b])


### 几何均值滤波

def GeometricMeanOperator(roi):
    roi = roi.astype(np.float64)
    p = np.prod(roi)

    return p ** (1/(roi.shape[0]*roi.shape[1]))


def GeometricMeanAlgorithm(image):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            new_image[i-1, j-1] = GeometricMeanOperator(image[i-1: i+2, j-1: j+2])
    new_image = (new_image - np.min(image)) * (255/np.max(image))

    return new_image.astype(np.uint8)


def rgbGeometricMean(image):
    r, g, b = cv2.split(image)
    r = GeometricMeanAlgorithm(r)
    g = GeometricMeanAlgorithm(g)
    b = GeometricMeanAlgorithm(b)

    return cv2.merge([r, g, b])


### 谐波均值
def HMeanOperator(roi):
    roi = roi.astype(np.float64)
    if 0 in roi:
        roi = 0
    else:
        roi = scipy.stats.hmean(roi.reshape(-1))

    return roi


def HMeanAlgorithm(image):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            new_image[i-1, j-1] = HMeanOperator(image[i-1: i+2, j-1: j+2])
    new_image = (new_image - np.min(image))*(255/np.max(image))
    return new_image.astype(np.uint8)


def rgbHMean(image):
    r, g, b = cv2.split(image)
    r = HMeanAlgorithm(r)
    g = HMeanAlgorithm(g)
    b = HMeanAlgorithm(b)

    return cv2.merge([r, g, b])


### 逆谐波均值
def IHMeanOperator(roi, q):
    roi = roi.astype(np.float64)

    return np.mean(roi ** (q + 1)) / np.mean(roi ** q)


def IHMeanAlogrithm(image, q):
    new_image = np.zeros(image.shape)
    image = cv2.copyMakeBorder(image, 1, 1, 1, 1, cv2.BORDER_DEFAULT)
    for i in range(1, image.shape[0]-1):
        for j in range(1, image.shape[1]-1):
            new_image[i-1, j-1] = IHMeanOperator(image[i-1: i+2, j-1: j+2], q)
    new_image = (new_image - np.min(image)) * (255/np.max(image))
    return new_image.astype(np.uint8)


def rgbIHMean(image, q):
    r, g, b = cv2.split(image)
    r = IHMeanAlogrithm(r, q)
    g = IHMeanAlogrithm(g, q)
    b = IHMeanAlogrithm(b, q)

    return cv2.merge([r, g, b])


if __name__ == '__main__':
    cat = cv2.imread('../pic/cat.jpg')
    cat = cv2.resize(cv2.cvtColor(cat, cv2.COLOR_BGR2RGB), (200, 200))
    spCat = SaltPepperNoisy(cat, 0.5, 0.1)
    gaussCat = GaussianNoisy(spCat, 25)
    # plt.subplot(121)
    # plt.title('Salt And Pepper Image')
    # plt.imshow(spCat)
    # plt.axis('off')
    # plt.subplot(122)
    # plt.imshow(gaussCat)
    # plt.axis('off')
    # plt.title('Gauss noise Image')
    # plt.show()

    # arith_sp_cat = rgbArithmeticMean(spCat)
    # gemo_sp_cat = rgbGeometricMean(spCat)
    # plt.subplot(121)
    # plt.title("Arithmetic to spImage")
    # plt.imshow(arith_sp_cat)
    # plt.axis("off")
    # plt.subplot(122)
    # plt.imshow(gemo_sp_cat)
    # plt.axis("off")
    # plt.title("Geomotric to spImage")
    # plt.show()

    # arith_gs_cat = rgbArithmeticMean(gaussCat)
    # gemo_gs_cat = rgbGeometricMean(gaussCat)
    # plt.subplot(121)
    # plt.title("Arithmetic to gsImage")
    # plt.imshow(arith_gs_cat)
    # plt.axis("off")
    # plt.subplot(122)
    # plt.imshow(gemo_gs_cat)
    # plt.axis("off")
    # plt.title("Geomotric to gsImage")
    # plt.show()

    # arith_sp_cat = rgbHMean(spCat)
    # gemo_sp_cat = rgbIHMean(spCat, 3)
    # plt.subplot(121)
    # plt.title("H Mean to spImage")
    # plt.imshow(arith_sp_cat)
    # plt.axis("off")
    # plt.subplot(122)
    # plt.imshow(gemo_sp_cat)
    # plt.axis("off")
    # plt.title("IH mean to spImage")
    # plt.show()

    arith_gs_cat = rgbHMean(gaussCat)
    gemo_gs_cat = rgbIHMean(gaussCat, 3)
    plt.subplot(121)
    plt.title("HMean to gsImage")
    plt.imshow(arith_gs_cat)
    plt.axis("off")
    plt.subplot(122)
    plt.imshow(gemo_gs_cat)
    plt.axis("off")
    plt.title("IHMean to gsImage")
    plt.show()






