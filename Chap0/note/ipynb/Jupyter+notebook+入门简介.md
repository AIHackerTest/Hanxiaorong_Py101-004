
# Jupyter notebook 软件的下载和安装

> 环境：Windows10家庭版，64位，已安装Python2.7.2和Python3.6.2

1、到官网[下载](https://www.continuum.io/downloads)Anaconda3软件安装包，Anaconda3集成了很多安装包，包括Python、Jupyter，所以安装Anaconda3就可

以，这样也省去了下载其他插件的麻烦，安装即可用。

2、点击安装包，直接全部点默认，一路安装下去即可。

3、安装完软件到开始菜单点击：开始——Anaconda3——anaconda prompt，打开自带的命令行，输入Jupyter notebook，电脑自动打开网页即表示安装成功。显示如图![1.png](attachment:1.png)

4、这只是Jupyter的安装，关于Python2和Python3的共存问题，Jupyter notebook 工作路径的更改等可以参考这里。[Python2 与 Python3 共存的问题](https://github.com/AIHackers/Py101-004/issues/25)

# Jupyter notebook日常操作

* Jupyther notebook 是一个可以把代码、图像、注释、公式和作图集于一处，从而实现可读性分析的一种灵活的工具。 **它的核心在于展示与快速迭代**。


* Jupyter 是以单元格的形式进行运行和工作的，可以通过anaconda prompt 输入Jupyter notebook和点击Jupter notebook快捷键的方式打开Jupyter。在正式编辑文档时先设置好工作路径。进入Jupyter，点这里新建文件：如图![2.png](attachment:2.png)，可以选择Python3或者text，如果是在Python2环境下，则显示Python2.这里有两种常用编辑模式，code和markdown。如图：![3.png](attachment:3.png)  在code编辑模式下，可以在单元格内输入命令，然后按Ctrl+Enter 运行，运行结果在单元格下面显示，同时左边会有数字显示本文档已经运行了多少次。如图：![4.png](attachment:4.png)  在markdown编辑模式下，按照Markdown的语法进行文本编辑，然后按Ctrl+Enter 运行，就会显示最终的效果。另外：markdown编辑时没有界面调整格式，只能用语法进行。[几个常用的markdown语法](http://www.jianshu.com/p/1e402922ee32/)


* Jupyter Notebook 有两种键盘输入模式。一、编辑模式，允许你往单元中键入代码或文本；这时的单元框线是绿色的。二、命令模式，对Jupyter的各种命令操作，这时的单元框线是蓝色的。按ESC或者CTRL+M，就进入命令模式，再按ENTRER就进入编辑模式。如图：![5.png](attachment:5.png)  


* 在Jupyter中编辑是自动保存的，在电脑任务栏点击Jupyter，可以查看每一步的操作指令记录。如图：![8.png](attachment:8.png)![7.png](attachment:7.png)     所以不用担心编辑的内容会丢失，另外，在断网的情况下，Jupyter notebook依然可以正常工作。编辑完后，可以选择导出自己想要的格式。方法如下：![6.png](attachment:6.png)


# Jupyter notebook 常用快捷键

* 使用Jupyter notebook 编辑充分掌握快捷键是非常便捷的。查看快捷键的方式如下：先按ESC键，进入命令模式，然后按 H 就可以查询相应的快捷键了。这里我截图了，是这样的：![jupyter%20%E5%BF%AB%E6%8D%B7%E9%94%AE.png](attachment:jupyter%20%E5%BF%AB%E6%8D%B7%E9%94%AE.png)![Jupyter%20%E5%BF%AB%E6%8D%B7%E9%94%AE2.png](attachment:Jupyter%20%E5%BF%AB%E6%8D%B7%E9%94%AE2.png)![jupyter%20%E5%BF%AB%E6%8D%B7%E9%94%AE3.png](attachment:jupyter%20%E5%BF%AB%E6%8D%B7%E9%94%AE3.png)


对英文不熟悉的话，可以下载金山词霸进行取词翻译，也可以利用谷歌翻译等。


# 小结：

* 以上就是对Jupyter notebook的简单操作，当然还有其他的很多命令，功能也应该是比较强大的。对于之前从来都没接触过这些工具，看完这个应该可以入门Jupyter notebook了。也可以参照其他人对Jupyter notebook的介绍。[探索Jupyter notebook
](https://github.com/Hanxiaorong/learnpython/blob/master/jupyter-notebook-turials.ipynb)
