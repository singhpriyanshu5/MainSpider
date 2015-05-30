  # -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import json

class JsonWriterPipeline(object):
    i=0
    x=0
    ss=''
    
    
    def __init__(self):
        with open('file_info.txt',"r") as f:
            for l in f:
                self.ss=l
                
        
                
        
        

    def process_item(self, item, spider):
        if self.x%500==0:
            self.i=self.i+1
            self.file = open('items_{}_{}.json'.format(self.ss,self.i), 'wb')    
        else:
            self.file = open('items_{}_{}.json'.format(self.ss,self.i), 'ab+')
           #self.file = open('items_%s_%d.json'%self.ss%self.i, 'ab+')               
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        self.x=self.x+1
        #print ss
        return item
