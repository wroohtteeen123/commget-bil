# Commget-Bil:

![Image_Commget-Bil](assets/github_commget-bil_logo.png)

## 这是什么？

它可以把一个用户发布的所有视频的所有评论塞到你的数据库里。

或者是把一个用户关注的其他用户发布的所有视频的所有评论塞到你的数据库里。

但这第二个功能好像还是不能用。

## 有什么用？

好吧，然后其实我也不知道有什么用啊，而且实际上写得不好，还有很多问题还是挺难用的的。

## 其他的呢？

数据库用的是MySQL。

上面这些话都是用Mac的F5识别出来的，所以说我也不知道对不对啦。

嗯嗯，如果你还要了解更多的话，你可以打开项目里的 OneMoreThing.md 。

## 用了什么东西：

    import os       # 用来删除文件。
    import ssl      # 用来更改链接方式？（我也不知道
    import time     # 把时间码转换成可读的时间。
    import math     # 计算 Av 号使用。
    import json     # 把 Json 转换成字典。
    import secrets  # 计算随机延时。

    import urllib.request   
    import urllib.parse
    import gzip
    import pymysql

    from pyfiglet import Figlet