# scrapy-demo
scrapy+splash+mangodb+分布式爬虫demo


### 安装splash

* 安装
前提是已经安装了docker，执行命令<br>
`docker pull scrapinghub/splash`<br>
这个要等非常久，因为服务器在国外，至少有1个G。
<br><br>
* 运行
安装完成后执行命令运行<br>
`docker run -p 8050:8050 -p 5023:5023 scrapinghub/splash`<br>
运行后可在浏览器打开localhost:8050就可以查看<br>
<br><br>
* 退出
退出不再是ctrl+c可以退出了，必须终端输入<br>
`docker ps`<br>
找出splash所在的CONTAINER ID，执行`docker kill id`命令就可以退出

### splash的基本配置

* 基本splash代码
```
function main(splash, args) {
    splash.images_enabled = false
    splash:go("https://www.baidu.com")
    return {
        html = splash:html()
    }   
}
```
* 控制浏览器插件是否开启，默认为false
```
splash.plugins_enabled = false 
```
* 控制页面上下左右滚动
```
splash.scroll_position = {x=100,y=100}
```
* go方法
<br>
`ok, reason = splash:go(url)`<br>
| 可配置参数               | 含义      | 
|:------------------------:|:-----------:|
| url                | 请求的url |
| baseurl                | 可选参数，默认为空，表示资源加载的相对路径 |
| headers                | 可选参数，默认为空，表示请求头 |
| http_method                | 可选参数，默认为GET |
| body                | 可选参数，默认为空，发送post请求的表单数据，使用的content-type为application/json |
| formdata                | 可选参数，默认为空，发送post请求的表单数据，使用的content-type为application/x-www-form-urlencoded |


      



