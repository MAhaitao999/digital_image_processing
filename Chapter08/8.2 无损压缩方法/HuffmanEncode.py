"""
Created by HenryMa on 2020/9/1
"""

__author__ = 'HenryMa'

from builtins import *


# 节点类
class Node(object):
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


# 哈夫曼树类
class HuffmanTree(object):
    # 根据Huffman树的思想: 以节点为基础, 反向建立Huffman树
    def __init__(self, char_weights):
        self.Leav = [Node(part[0], part[1]) for part in char_weights]  # 根据输入的字符及其频数生成节点
        while len(self.Leav) != 1:
            self.Leav.sort(key=lambda node: node.value, reverse=True)
            c = Node(value=(self.Leav[-1].value+self.Leav[-2].value))
            c.left = self.Leav.pop(-1)
            c.right = self.Leav.pop(-1)
            self.Leav.append(c)
        self.root = self.Leav[0]
        self.Buffer = list(range(10))

    # 用递归的思想生成编码
    def pre(self, tree, length):
        node = tree
        if not node:
            return
        elif node.name:
            print(node.name + ' encoding:', end='')
            for i in range(length):
                print(self.Buffer[i], end='')
            print('\n')
            return
        self.Buffer[length] = 0
        self.pre(node.left, length+1)
        self.Buffer[length] = 1
        self.pre(node.right, length+1)

    # 生成Huffman编码
    def get_code(self):
        self.pre(self.root, 0)


if __name__ == '__main__':
    # 输入的是字符及其频数
    char_weights = [('a', 6), ('b', 4), ('c', 10), ('d', 8), ('f', 12), ('g', 2)]
    tree = HuffmanTree(char_weights)
    tree.get_code()





