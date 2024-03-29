# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:57:20 2018

@author: 13758
"""
import random
import urllib.request
from lxml import etree
import requests
import os

class myspider:
    def __init__(self):
        self.tieba_name = input("Name of Tieba:")
        self.tieba_begin_page = int(input("Begin page："))
        self.tieba_end_page = int(input("End page："))
        cwd = os.getcwd()
        if not os.path.exists(os.path.join(cwd, '贴吧')):
            os.makedirs(os.path.join(cwd,'贴吧'))
            
        self.tieba_dirs = os.path.join(cwd, '贴吧')
        
        
        self.url = 'http://tieba.baidu.com/f'
        self.img_number= 1
    def spider_tieba(self):
        for item in range(self.tieba_begin_page,self.tieba_end_page+1):
            ua_list = [ "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
                        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
                        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
                        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
                        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
                        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
                        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
                        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
                        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
                        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
                        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
                        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
                        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
                        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
                        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52"
                        ]         
            page = (item-1)*50
            self.ua = {'User-agent':random.choice(ua_list)}
            word = {'kw': self.tieba_name,'pn':page}

            response = requests.get(self.url,params = word,headers = self.ua)
            
            html = response.text
            selector = etree.HTML(html)
            links = selector.xpath('//div[@class="threadlist_lz clearfix"]/div/a/@href')

            for link in links:
                img_url = "http://tieba.baidu.com"+link
                self.img_load(img_url)
                
    def img_load(self, img_url):

        html = requests.get(img_url, headers = self.ua).text

        img_xml = etree.HTML(html)
        img_links = img_xml.xpath('//img[@class="BDE_Image"]/@src')

        for img in img_links:
            self.img_download(img)
            
    
    def img_download(self, img):
        
        print("Downloading image %d" %self.img_number)
        self.f = open(self.tieba_dirs+'/'+str(self.img_number)+".jpg", 'wb')

        images = urllib.request.urlopen(img).read()
        self.f.write(images)
        self.img_number += 1


if __name__ == '__main__':
    spider = myspider()
    spider.spider_tieba()
    
    print("Finish")

