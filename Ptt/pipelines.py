# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import date, datetime
import json
import codecs

class PttPipeline:
    # def __init__(self):
    #     self.file = codecs.open('gossipping_utf8.json', 'wb', encoding='utf-8')


    # def process_item(self, item, spider):
        
    #     line = json.dumps(dict(item),cls=ComplexEncoder) +"\n"
    #     print("line",type(line))
    #     self.file.write(line.encode('utf-8').decode('unicode_escape'))

    #     return item
    def process_item(self, item, spider):
        return item
# class ComplexEncoder(json.JSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, datetime):
#             return obj.strftime('%Y-%m-%d %H:%M:%S')
#         elif isinstance(obj, date):
#             return obj.strftime('%Y-%m-%d')
#         else:
#             return json.JSONEncoder.default(self, obj)