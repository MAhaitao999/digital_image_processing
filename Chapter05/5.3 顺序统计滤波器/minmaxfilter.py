import cv2
import matplotlib.pyplot as plt
import math


def max_filter(image, ksize=3):
    """
    最大值滤波函数
    :param image: 输入要图像
    :param ksize: 模板尺寸
    :return: 滤波结果图像
    """
    border_width = int((ksize-1)/2)  # 边界填充宽度
    # 填充便捷操作
    border_filling = cv2.copyMakeBorder(image,
                                        border_width, border_width, border_width, border_width,
                                        cv2.BORDER_REPLICATE)
    max_image = image.copy()
    for i in range(border_width, border_filling.shape[0]-border_width):
        for j in range(border_width, border_filling.shape[1]-border_width):
            # 读取模板下像素的灰度值
            lists = []
            for s in range(i-border_width, i+border_width+1):
                for t in range(j-border_width, j+border_width+1):
                    lists.append(border_filling[s][t])
            # 选最大值作为输出图像模板中心像素的灰度值
            max_image[i-border_width][i-border_width] = max(lists)
    return max_image


def min_filter(image, ksize=3):
    """
    最小值滤波函数
    :param image:输入图像
    :param ksize:模板尺寸
    :return:滤波结果图像
    """
    border_width = int((ksize-1)/2)  # 边界填充宽度
    # 填充边界操作
    border_filling = cv2.copyMakeBorder(image,
                                        border_width, border_width, border_width, border_width,
                                        cv2.BORDER_REPLICATE)
    # 从[(ksize-1)/2, (ksize-1)/2]开始向右下角进行漫游重合，
    # 到[borderFilling.shape[0]-3, borderFilling.shape[1]-3]停止
    min_image = image.copy()
    for i in range(border_width, border_filling.shape[0]-border_width):
        for j in range(border_width, border_filling.shape[1]-border_width):
            # 读取模板下像素的灰度值
            lists = []
            for s in range(i-border_width, i+border_width+1):
                for t in range(j-border_width, j+border_width+1):
                    lists.append(border_filling[s][t])
            # 选最大值作为输出图像模板中心像素的灰度值
            min_image[i-border_width][j-border_width] = min(lists)
    return min_image


# 显示函数
def show_images(images):
    for i in range(len(images)):
        img = images[i]
        # 行，列，索引
        x = 2
        plt.subplot(x, math.ceil(len(images) / x), i + 1)
        plt.imshow(img, cmap="gray")
        title = "(" + str(i + 1) + ")"
        plt.title(title, fontsize=10)
        plt.xticks([])
        plt.yticks([])
    plt.show()


if __name__ == '__main__':
    image = cv2.imread("../pic/cat.jpg", 0)
    image = cv2.resize(image, (200, 200))
    maxFilter1 = max_filter(image, 3)
    maxFilter2 = max_filter(maxFilter1, 3)
    maxFilter3 = max_filter(maxFilter2, 3)
    minFilter1 = min_filter(image, 3)
    minFilter2 = min_filter(minFilter1, 3)
    minFilter3 = min_filter(minFilter2, 3)
    imgs = [image, maxFilter1, maxFilter2, maxFilter3, image, minFilter1, minFilter2, minFilter3]
    show_images(imgs)
