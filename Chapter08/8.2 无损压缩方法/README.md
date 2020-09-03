### 无损压缩

- 减少像素间冗余

- 减少编码冗余

#### 变长编码

将最短的码字赋给概率最大的灰度级, 只减少编码冗余.

##### B编码

![](../pic/B编码.png)

![](../pic/B1编码实例.png)

![](../pic/B2编码实例.png)

##### Huffman编码

当对信源符号逐个编码时, Huffman编码能给出最短的码字.

![](../pic/Huffman编码1.png)

![](../pic/Huffman编码2.png)

使用Huffman编码需要注意的问题:

![](../pic/使用Huffman编码需要注意的问题.png)

Huffman编码的优化:

![](../pic/Huffman编码的优化算法.png)

![](../pic/变长编码.png)

##### 移位码(S码)

![](../pic/移位码.png)

![](../pic/S2编码例子.png)

Huffman移位编码

![](../pic/Huffman移位编码.png)

##### 算术编码

![](../pic/算术编码1.png)

![](../pic/算术编码2.png)

![](../pic/算术编码例子.png)

![](../pic/算术编码例子2.png)

![](../pic/算术编码3.png)

![](../pic/算术编码4.png)

