日々私たちが過ごしている日常は、実は、奇跡の連続なのかもしれない。

我们所经历的每个平凡的日常，也许就是连续发生的奇迹。&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——《日常》

---

#### 使用方法：

#### 1. 反向代理：

将P站图片网址中的 <font color=#0051af>i.pximg.net</font> 替换为 <font color=#0051af>i.muxmus.com:5000</font>

例如：

https://<font color=#0051af>i.pximg.net</font>/img-original/img/2011/11/05/00/32/32/22848009_p0.jpg

↓

https://<font color=#0051af>i.muxmus.com:5000</font>/img-original/img/2011/11/05/00/32/32/22848009_p0.jpg

#### 2. 通过图片id抓取原图（实验性）：

<font color=#b00000>! 实验性功能，建议仅在无法获取原图网址时使用 !</font>

格式：

+ 单张，一个id中只有一张图片或多张中的第一张：https://i.muxmus.com:5000/<font color=#0051af>id</font>

→ https://i.muxmus.com:5000/<font color=#0051af>22848009</font>

+ 多张（漫画、组图），一个id中有多张图片：

https://i.muxmus.com:5000/<font color=#0051af>id</font>-<font color=#0051af>第几张</font>

→ https://i.muxmus.com:5000/<font color=#0051af>22848009</font>-<font color=#0051af>1</font>

*   自定义扩展名：

    https://i.muxmus.com:5000/<font color=#0051af>id</font>.<font color=#0051af>扩展名</font>

    → https://i.muxmus.com:5000/<font color=#0051af>22848009</font>.<font color=#0051af>jpg</font>

    https://i.muxmus.com:5000/<font color=#0051af>id</font>-<font color=#0051af>第几张</font>.<font color=#0051af>扩展名</font>

    → https://i.muxmus.com:5000/<font color=#0051af>22848009</font>-<font color=#0051af>1</font>.<font color=#0051af>jpg</font>

注意事项：

*	id：作品页网址最后的一串数字，如“https://www.pixiv.net/artworks/22848009”当中的“22848009”。 [什么是作品ID？](https://www.pixiv.help/hc/zh-cn/articles/235585168-%E4%BB%80%E4%B9%88%E6%98%AF%E4%BD%9C%E5%93%81ID)

*   该功能通过爬取id对应的html页面获取原图网址，并进行重定向。但由于只能得到第一张的网址，如果是多图的话，第一张以外的扩展名都是未知的，所以只能默认都采用第一张的扩展名。如果因默认的扩展名错误而404，请采用上面的第三种格式，自定义扩展名。

*   P站的动图并非gif而是多张jpg循环播放，如果请求的是动图，会返回第一帧的jpg。

*   P站的图片扩展名目前有且仅有jpg(jpeg)、png、gif三种，注意此处的gif并非gif动图，只是gif格式的静态图片。 [可以在pixiv上投稿什么图片格式](https://help.pixiv.digital/hc/zh-cn/articles/235584428-%E5%8F%AF%E4%BB%A5%E5%9C%A8pixiv%E4%B8%8A%E6%8A%95%E7%A8%BF%E4%BB%80%E4%B9%88%E5%9B%BE%E7%89%87%E6%A0%BC%E5%BC%8F)&nbsp;&nbsp;[如何在pixiv上投稿插画？](https://www.pixiv.help/hc/zh-cn/articles/235584588-%E5%A6%82%E4%BD%95%E5%9C%A8pixiv%E4%B8%8A%E6%8A%95%E7%A8%BF%E6%8F%92%E7%94%BB)
