日々私たちが過ごしている日常は、実は、奇跡の連続なのかもしれない。

我们所经历的每个平凡的日常，也许就是连续发生的奇迹。&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;——《日常》

---

#### 使用方法：

#### 1. 反向代理：

将P站图片网址中的 <font color=#0051af>i.pximg.net</font> 替换为 <font color=#0051af>i.muxmus.com</font>

例如：

https://<font color=#0051af>i.pximg.net</font>/img-original/img/2011/11/05/00/32/32/22848009_p0.jpg

↓

https://<font color=#0051af>i.muxmus.com</font>/img-original/img/2011/11/05/00/32/32/22848009_p0.jpg

#### 2. 通过图片id抓取原图（实验性）：

<font color=#b00000>! 实验性功能，建议仅在无法获取原图网址时使用 !</font>

格式：

+ 单张，一个id中只有一张图片或多张中的第一张：

	https://<font>i.muxmus.com/</font><font color=#0051af>id</font>
 
 	https://<font>i.muxmus.com/</font><font color=#0051af>22848009</font>

+ 多张（漫画、组图），一个id中有多张图片：

	https://<font>i.muxmus.com/</font><font color=#0051af>id</font>-<font color=#0051af>第几张</font>
 
	https://<font>i.muxmus.com/</font><font color=#0051af>22848009</font>-<font color=#0051af>1</font>

+ 指定扩展名（优先级较高，非必要请勿使用，如需使用请确保指定的扩展名正确）：

	https://<font>i.muxmus.com/</font><font color=#0051af>id</font>.<font color=#0051af>扩展名</font>
 
	https://<font>i.muxmus.com/</font><font color=#0051af>22848009</font>.<font color=#0051af>jpg</font>

	https://<font>i.muxmus.com/</font><font color=#0051af>id</font>-<font color=#0051af>第几张</font>.<font color=#0051af>扩展名</font>
 
	https://<font>i.muxmus.com/</font><font color=#0051af>22848009</font>-<font color=#0051af>1</font>.<font color=#0051af>jpg</font>

注意事项：

*  id：作品页网址最后的一串数字，如“https://<font>www</font>.pixiv.<font>net/artworks/22848009”当中的“22848009”。</font> [什么是作品ID？](https://www.pixiv.help/hc/zh-cn/articles/235585168-%E4%BB%80%E4%B9%88%E6%98%AF%E4%BD%9C%E5%93%81ID)

*  该功能通过爬取id对应的html页面获取原图网址，并进行代理。由于只能得到第一张图片的网址，多张的话，第一张之外的扩展名都是未知的，所以默认都采用第一张的扩展名。但由[可以在pixiv上投稿什么图片格式](https://www.pixiv.help/hc/zh-cn/articles/235584428-%E5%8F%AF%E4%BB%A5%E5%9C%A8pixiv%E4%B8%8A%E6%8A%95%E7%A8%BF%E4%BB%80%E4%B9%88%E5%9B%BE%E7%89%87%E6%A0%BC%E5%BC%8F)可知，目前在P站如果同时投稿多种格式的图片，P站会将其全部转换为jpg。所以第三种格式——指定扩展名好像没什么用，只能说战未来！万一哪天P站不帮忙转格式了呢（绝对不是因为我写程序前没看官方的帮助文档）。

*  P站的动图并非gif而是多张jpg循环播放，如果请求的是动图，会返回第一帧的jpg。

*  P站的图片扩展名目前有且仅有jpg、png、gif三种，注意此处的gif并非gif动图，只是gif格式的静态图片。[可以在pixiv上投稿什么图片格式](https://www.pixiv.help/hc/zh-cn/articles/235584428-%E5%8F%AF%E4%BB%A5%E5%9C%A8pixiv%E4%B8%8A%E6%8A%95%E7%A8%BF%E4%BB%80%E4%B9%88%E5%9B%BE%E7%89%87%E6%A0%BC%E5%BC%8F)&nbsp;&nbsp;[如何在pixiv上投稿插画？](https://www.pixiv.help/hc/zh-cn/articles/235584588-%E5%A6%82%E4%BD%95%E5%9C%A8pixiv%E4%B8%8A%E6%8A%95%E7%A8%BF%E6%8F%92%E7%94%BB)
