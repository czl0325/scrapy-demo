import requests

# 在运行了splash的情况下请求百度页面
response = requests.get("http://localhost:8050/render.html?url=https://www.baidu.com")
print(dir(response))