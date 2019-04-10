# -*- coding: utf-8 -*-
import scrapy
from pafeng.items import PafengItem

class FenghuangSpider(scrapy.Spider):
    name = 'fenghuang'
    allowed_domains = ['news.ifeng.com']
    start_urls = ['http://news.ifeng.com/ipad/']

    def parse(self, response):
        titles = response.xpath("//ul[@class='clearfix']/li/a/text()").extract()
        tithrefs = response.xpath("//ul[@class='clearfix']/li/a/@href").extract()
        # print(titles)
        # print(tithrefs)
        for title, tithref in zip(titles, tithrefs):
            data = {'title': title, 'tithref': tithref}
            # print(tithrefs)
            yield scrapy.Request(tithref, meta={'data': data}, callback=self.getNewList)

    def getNewList(self, response):
        data = response.meta['data']
        title = data['title']
        tithref = data['tithref']
        litis=[]
        conlitis=[]
        days = []
        if title == "国际" or title == "大陆" or title == "台湾" or title == "社会" :
            litis += response.xpath("//div[@class='juti_list']/h3/a/text()").extract()
            conlitis += response.xpath("//div[@class='juti_list']/h3/a/@href").extract()
            # days += response.xpath("//div[@class='ping03']/span/text()").extract()
        if title == "即时":
            litis += response.xpath("//div[@class='newsList']/ul/li/a/text()").extract()
            conlitis += response.xpath("//div[@class='newsList']/ul/li/a/@href").extract()
            # days += response.xpath("//div[@class='newsList']/ul/li/h4/text()").extract()
        if title == "深度":
            litis += response.xpath("//div[@class='zheng_list pl10 box clearfix']/h2/a/text()").extract()
            conlitis += response.xpath("//div[@class='zheng_list pl10 box clearfix']/h2/a/@href").extract()
            # days += response.xpath("//div[@class='Function']/a/text()").extract()
        if title == "专题" :
            litis += response.xpath("//ul[@class='clearfix']/li/a/text()").extract()
            conlitis += response.xpath("//ul[@class='clearfix']/li/a/@href").extract()
            # days += response.xpath("//ul[@class='clearfix']/li/span/text()").extract()
        if  title == "排行":
            for i in range(1,9):
                litis += response.xpath("//div[@id='c0%s']/table/tbody/tr/td[2]/h3/a/text()" % i).extract()
                conlitis += response.xpath("//div[@id='c0%s']/table/tbody/tr/td[2]/h3/a/@href" % i).extract()
            # days += response.xpath("//div[@class='ping03']/span/text()").extract()
        if title == "大鱼漫画":
            litis += response.xpath("//div[@class='con_lis']/a/h4/text()").extract()
            conlitis += response.xpath("//div[@class='con_lis']/a/@href").extract()
            days += response.xpath("//ul[@class='clearfix']/li/span/text()").extract()
        if title == "暖新闻" or title == "宣战2020":
            litis += response.xpath("//div[@class='con_lis']/a/div/h4/text()").extract()
            conlitis += response.xpath("//div[@class='con_lis']/a/@href").extract()
            # days += response.xpath("//div[@class='con_lis']/a/div/p/text()").extract()
        if title == "大参考":
            litis += response.xpath("//div[@class='pictxt']/h2/a/text()").extract()
            conlitis += response.xpath("//div[@class='pictxt']/h2/a/@href").extract()
        if title == "新闻联播必读" :
            litis += response.xpath("//div[@class='con_lis']/a/div/h4/text()").extract()
            conlitis += response.xpath("//div[@class='con_lis']/a/@href").extract()
            # days += response.xpath("//div[@class='con_lis']/a/div/p/text()").extract()

        # print(litis,conlitis,days)

        if litis and conlitis:
            for liti, conliti in zip(litis, conlitis):
                item = PafengItem()
                item['title'] = title
                item['tithref'] = tithref
                item['liti'] = liti
                item['conliti'] = conliti
                # item['day'] = day
                yield scrapy.Request(conliti, meta={'item': item}, callback=self.getNewCon)

    def getNewCon(self, response):
            item = response.meta['item']
            if item['title']== "国际" or item['title']== "大陆" or item['title']== "台湾" or item['title']== "社会" or item['title'] == "排行":
                 item['day'] = response.xpath("//span[@class='ss01']/text()").extract()
                 item['author'] = response.xpath("//span[@class='ss03']/a/text()").extract()
                 item['con'] = response.xpath("//div[@id='main_content']/p/text()").extract()

            if item['title']== "大鱼漫画":
                 item['day'] = response.xpath("//div[@class='yc_tit']/p/span[1]/text()").extract()
                 item['author'] = response.xpath("//div[@class='yc_tit']/p/a/text()").extract()
                 item['con'] = response.xpath("//div[@id='js_content']/p/text()").extract()
            if item['title']== "暖新闻" or item['title']== "宣战2020" or item['title'] == "新闻联播必读":
                 item['day'] = response.xpath("//div[@class='yc_tit']/p/span/text()").extract()
                 item['author'] = response.xpath("//div[@class='yc_tit']/p/a/text()").extract()
                 item['con'] = response.xpath("//div[@id='yc_con_txt']/p/text()").extract()
            if item['title']== "大参考" :
                 item['day'] = response.xpath("//div[@class='stoBigPicCon']/span/text()").extract()
                 item['author'] = response.xpath("//div[@class='stoBigPicCon']/span/text()").extract()
                 item['con'] = response.xpath("//div[@class='stoConTxt02']/p/text()").extract()
            return item