# nuist校园网登陆和注销
## 环境

python3

使用库：request和 base64

## 使用

安装python3环境和pip 相应的包之后

修改login.py文件里面的**账号，密码，运行商（这很重要）**

logout.py文件什么都不需要修改。。

### windows

感觉直接使用命令python3 login.py的话 速度有点慢

建议打包成exe使用，具体打包方法百度一下，你就知道

#### 具体流程

连接上i-NUIST无线网之后

直接运行login.py打包成的文件，账号密码没错的话就能登陆成功了。

想注销就直接运行logout打包成的文件

#### 屏蔽烦人的弹窗

连接上无线网之后的登陆网页弹窗，你可以完全忽略它。

如果，想屏蔽它，那也有方法

打开注册表，[教程](https://jingyan.baidu.com/article/ce09321bbc57df2bff858fd0.html)

HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\NlaSvc\Parameters\Internet

中的enableactiveprobing

设置成0就行了

### mac

mac运行速度比较快，使用命令python3 login.py就行了

具体就是，创建一个command文件

里面写

```shell
cd login.py的文件夹地址
python3 login.py
```

修改一下cd后面的文件夹地址

然后保存一下**登陆.command**文件

放到桌面上就行使用了

注销也是同理

```shell
cd logout.py的文件夹
python3 logout.py
```

修改一下cd后面的文件夹地址

#### 具体流程

连接上i-NUIST无线网之后

把弹出的网页给取消了（command+q都关不掉，我哭了）

运行command文件就行了



#### 关于弹窗

mac系统我找不到方法啊😭，谁能告诉我怎么屏蔽它。每次都要手动取消它，真的很烦唉。



## 原理

先凑合看看我以前在[csdn](https://blog.csdn.net/u010651394/article/details/82975266)上写的吧



