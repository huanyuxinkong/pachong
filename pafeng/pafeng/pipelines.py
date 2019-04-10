# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class PafengPipeline(object):
    def process_item(self, item, spider):
        if item['author']:
            with open('db.txt', 'a',encoding='utf-8') as f:
                f.write("%s %s %s %s %s %s %s" % (item['title'], item['tithref'], item['liti'], item['conliti'], item['author'], item['con'], item['day']))
                f.write("\n")

        else:

            with open('db.txt', 'a', encoding='utf-8') as f:
                f.write("%s %s %s %s" % (item['title'], item['tithref'], item['liti'], item['conliti']))
                f.write("\n")
        return item
