from lxml import etree
import requests
import MyQR

res = requests.get('http://www.santostang.com/2018/07/11/《网络爬虫：从入门到实践》一书勘误/')
webdata = res.text
data =etree.HTML(webdata)
print(data.xpath('//*[@id="main"]/article/h1/text()')[0])