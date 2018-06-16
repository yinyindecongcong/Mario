---

typora-root-url: C:\Users\Administrator\Desktop\all\typora\image_md\mario
typora-copy-images-to: C:\Users\Administrator\Desktop\all\typora\image_md\mario
---

## A LAN Game: Super Mario 

* This is a python project of Super Mario, learning from [justinmeister/Mario-Level-1](https://github.com/justinmeister/Mario-Level-1).
* [ppzqh](https://github.com/ppzqh) and me finish the task together, And we have finished that making it a LAN game, you can play the **2-PLAYER mode** on two PC. 

### 简介

* 这是一个超级马里奥游戏的第一关的实现，有单人和双人两种模式，其中双人模式由CS下的帧同步实现。
  * （P2P下的帧同步实现过程中遇到一些问题，没能解决，故使用CS下的帧同步）
* 该游戏基于pygame实现

### 使用说明

* 单人模式下，直接运行**main.py**并选择单人模式即可

* 双人模式下，由于使用CS下的帧同步，增加了**server.py**负责收发信息
  * 为了简单，我们要求双方知道对方的IP地址及端口，并将其中一方作为服务器，并在**config.py**中正确设置
  * **server.py**在一台电脑运行，**main.py**在各自电脑运行，三次运行顺序没有规定

* 运行情况如下：

#####单人模式

<img src="http://chuantu.biz/t6/329/1529136015x1822611287.png">
<img src="http://chuantu.biz/t6/329/1529137170x-1404775503.gif">

  

#####双人模式

<img src="http://chuantu.biz/t6/329/1529137664x-1404775503.gif">



  