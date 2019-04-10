import requests
from urllib.request import *
from fake_useragent import UserAgent
from lxml.etree import HTML
import time,pickle

#爬取招聘信息


# url = "https://www.liepin.com/zhaopin/?d_headId=e191b4c15d4efad10d26eb5330adb953&curPage="
# urls = [url+str(i) for i in range(1, 10)]
#
#
# ua = UserAgent()
# headers = {
#     "User-Agent": "ua.random"
# }
#
#
# data = []
#
#
# def sp(lin):
#     res = requests.get(url, headers=headers)
#     doc = HTML(res.text)
#
#     def value(lenss):
#         link = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[1]/h3/a/@href") % lenss)
#         title = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[1]/h3/@title") % lenss)
#         money = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[1]/p[1]/span[1]/text()") % lenss)
#         place = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[1]/p[1]/a/text()") % lenss)
#         efu = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[1]/p[1]/span[@class='edu']/text()") % lenss)
#         experience = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[1]/p[1]/span[3]/text()") % lenss)
#         name = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[last()]/p[1]/a/text()") % lenss)
#         types = doc.xpath(("//ul[@class='sojob-list']/li[%s]/div[1]/div[last()]/p[2]/span/a/text()") % lenss)
#         return {
#             'link': link,
#             'title': title,
#             'money': money,
#             'place': place,
#             'efu': efu,
#             'experience': experience,
#             'name': name,
#             'types': types
#         }
#
#     mm = []
#     for m in range(1, 41):
#         arr = value(m)
#
#         mm.append(arr)
#     return mm
#     # print(data)
#
#
# ind = 1
# for lin in urls:
#     ind +=1
#     time.sleep(1)
#     sp(lin)
#     data.append(sp(lin))
#
#
# with open("./exe.txt",'wb') as f:
#     pickle.dump(data, f)
#     print("xie")
#
#
#
# with open("./exe.txt", 'rb') as f:
#     li = pickle.load(f)
#     # print("xie")
# import  xlwt, pickle   # 写入excl
#
# wb = xlwt.Workbook()    # 创建表格对像
# ws = wb.add_sheet("招聘信息")  # 创建表
#
# index = 0
# for arr2 in li:
#     for ll in arr2:
#         # 序号
#         ws.write(index, 0,  ll['link'])
#
#         ws.write(index, 1, ll['title'])
#
#         ws.write(index, 2, ll['money'])
#         ws.write(index, 3, ll['place'])
#
#         ws.write(index, 4, ll['title'])
#
#         ws.write(index, 5, ll['efu'])
#         ws.write(index, 6, ll['experience'])
#
#         ws.write(index, 7, ll['name'])
#
#         ws.write(index, 8, ll['types'])
#         index += 1
#
# wb.save('exe.xls')
# #

