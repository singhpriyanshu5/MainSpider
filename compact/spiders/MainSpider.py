import scrapy
from compact.items import CompactItem
from compact.config import Config
from compact.websites import cardekho, gaadi, cartrade
import sys
#from scrapy import signals
#from scrapy.xlib.pydispatch import dispatcher

def str_to_class(str2):
    return getattr(sys.modules[__name__], str2)

class MainSpider(scrapy.Spider):
    name="mainspider"
    start_page=2
    end_page=60
    strr=''
    source2=''
    conf2=Config()
    count=0
    
    def __init__(self,stra=''):
        self.strr=stra
        self.source2=str_to_class(self.strr)
        with open("file_info.txt", "w") as text_file:
            text_file.write("%s"%self.strr)
        #dispatcher.connect(self.spider_closed, signals.spider_closed)
    
    

    def get_config(self,source):
        conf=Config()
        conf.sel=source.sel
        conf.city=source.city
        conf.model=source.model
        conf.yom=source.yom
        conf.price=source.price
        conf.kms=source.kms
        conf.transm=source.transm
        conf.fuel=source.fuel
        conf.owner=source.owner
        conf.url=source.url
        conf.url1=source.url1
        conf.url2=source.url2
        conf.color=source.color
        return conf
    
        

    def start_requests(self):
        self.conf2=self.get_config(self.source2)
        yield self.make_requests_from_url(self.conf2.url1)
        for i in range(self.start_page,self.end_page+1):
            yield self.make_requests_from_url(self.conf2.url2%i)

    def get_count(self):
        return self.count
            
    
    def parse(self,response):
        #print response.xpath(self.conf2.sel)
        item=CompactItem()
        countt=0
        for sel in response.xpath(self.conf2.sel):
            countt=countt+1
            #self.count=self.count+1
            if self.strr=="gaadi":
                if countt==3:
                    continue
            item['model']=sel.xpath(self.conf2.model).extract()
            item['price']=sel.xpath(self.conf2.price).extract()
            item['kms']=sel.xpath(self.conf2.kms).extract()
            item['fuel']=sel.xpath(self.conf2.fuel).extract()
            item['city']=sel.xpath(self.conf2.city).extract()
            item['url']=sel.xpath(self.conf2.url).extract()
            item['color']=sel.xpath(self.conf2.color).extract()
            item['transm']=sel.xpath(self.conf2.transm).extract()
            if self.strr=="cartrade":
                model_str=''.join(item['model'])
                yom1=model_str.split('(')
                yom2=yom1[1].split(')')
                item['yom']=yom2[0]
            elif self.strr=="cardekho":
                yom_str=''.join(sel.xpath(self.conf2.yom).extract())
                yom2=yom_str.split(' ')
                item['yom']=yom2[0]
                str_price=''.join(item['price'])
                str_stripped_price=" ".join(str_price.split())
                item['price']=str_stripped_price
            elif self.strr=="gaadi":
                item['yom']=sel.xpath(self.conf2.yom).extract()
                del item['city'][-1]
            
            
            #if self.strr!="gaadi":
            item['owner']=sel.xpath(self.conf2.owner).extract()
            yield item
            
               # url_str=''.join(item['url'])
               # request=scrapy.Request(url_str, callback=self.parse2)
               # request.meta['item']=item
               # yield request
            
  
    #def parse2(self,response):
    #    item=response.meta['item']
    #    if response.xpath('//div[@id="pagecontent"]/div/div[2]/div[2]/article/div[5]/div[2]/table/tbody/tr[1]/td[4]'):
    #        item['owner']=response.xpath('//div[@id="pagecontent"]/div/div[2]/div[2]/article/div[3]/ul/li[5]/strong/text()').extract()
    #    else:
    #        item['owner']=response.xpath('//div[@id="pagecontent"]/div/div[2]/div[1]/article/div[3]/ul/li[5]/strong/text()').extract()
        
    #   yield item
        
    #def spider_closed(self, spider):
     #   with open("file_info.txt", "w") as text_file:
      #      text_file.write("%s\n" %self.strr) 
        
      # second param is instance of spder about to be closed.

    
    
