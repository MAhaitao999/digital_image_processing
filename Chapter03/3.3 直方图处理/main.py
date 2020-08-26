"""
Created by HenryMa on 2020/8/26
"""

__author__ = 'HenryMa'


from PIL import Image, ImageOps
import numpy as np
from builtins import print

from contrast import ImageContraster


if __name__ == '__main__':
    # read image
    img = Image.open('../pic/Fig0320(4)(bottom_left).tif')
    print(np.array(img).shape)

    # contraster
    icter = ImageContraster()

    # HE
    he_eq_img = icter.enhance_contrast(img, method='HE')
    icter.plot_images(img, he_eq_img)

    # AHE
    ahe_eq_img = icter.enhance_contrast(img, method='AHE', window_size=32, affect_size=16)
    icter.plot_images(img, ahe_eq_img)

    # CLANE
    clane_eq_img = icter.enhance_contrast(img, method='CLANE', blocks=8, threshold=10.0)
    icter.plot_images(img, clane_eq_img)

    # Local Region Stretch
    lrs_eq_img = icter.enhance_contrast(img, method='Bright')
    icter.plot_images(img, lrs_eq_img)




