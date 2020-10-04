import urllib
from urllib import request
from lxml import etree
import os
url="https://minecraft-zh.gamepedia.com/%E9%A3%9F%E7%89%A9/"
header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
}
savePath="C:/Users/zyw/Desktop/PStest/MC/food/"
def getPage():#获取页面
    req = urllib.request.Request(url=url, headers=header)#发起请求
    html = urllib.request.urlopen(req)#打开链接
    htmldata = html.read()#获取HTML
    htmlpath = etree.HTML(htmldata)#解析HTML
    pages = htmlpath.xpath('//th[@scope="row"]/a/@href')#找到目标内容
    for i in pages:
        pagesitem = "https://minecraft-zh.gamepedia.com" + i.encode().decode()
        getItem(pagesitem)

def getItem(pagesitem):#获取高清图片所在页面
    req = urllib.request.Request(url=pagesitem, headers=header)
    html = urllib.request.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)
    items = htmlpath.xpath('//div[@class="infobox-imagearea"]/div/a/@href')
    imgname = htmlpath.xpath('//h1[@itemprop="name"]')
    for i in items:
        itemsimg = "https://minecraft-zh.gamepedia.com" + i.encode().decode()
        getImg(itemsimg,imgname)

def getImg(itemsimg,imgname):#获取高清图片
    req = urllib.request.Request(url=itemsimg, headers=header)
    html = urllib.request.urlopen(req)
    htmldata = html.read()
    htmlpath = etree.HTML(htmldata)
    imgspath = htmlpath.xpath('//div[@class="fullImageLink"]/a/@href')
    for i in imgspath:
        imgpath = i.encode().decode()
        urllib.request.urlretrieve(imgpath,savePath+imgname+".png")

if __name__ == '__main__':
    getPage()