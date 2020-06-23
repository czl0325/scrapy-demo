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


