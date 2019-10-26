# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 10:40:24 2018

@author: 13758
"""

import requests
import os
import random
from lxml import etree

class ganji:
    
    def __init__(self):
        self.count = 1
        self.begin_page = int(input('Begin Page:'))
        self.end_page = int(input('End Page:'))
        cwd = os.getcwd()
        if not os.path.exists(os.path.join(cwd, '赶集网')):
            os.makedirs(os.path.join(cwd,'赶集网'))
            
        self.Ganji_dirs = os.path.join(cwd, '赶集网')
        self.f = open(self.Ganji_dirs+'/'+'ganji'+'.text', 'w')
        
        
    def load_page(self):
        for pn in range(self.begin_page, self.end_page):
            url= 'http://hf.ganji.com/zpxuetugong/o'+str(pn)+'/'
            
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
            try:
                ua = {'User-agent':random.choice(ua_list)}
                html = requests.get(url, headers = ua).text
                html = etree.HTML(html)
                
                list_links = html.xpath('//div[@data-widget="app/ms_v2/wanted/list.js#companyAjaxBid"]/dl')
                
            except Exception as e:
                print("Loadpage:",e)
            for item in list_links:
                self.data_search(item)
                
    
    def data_search(self, link):

        try:
            salary = str(link.xpath('./dd[@class="company"]/div[@class="new-dl-salary"]/text()'))
            salary = salary.replace(" ", '')
            min_salary = salary[4:8]
            max_salary = salary[9:13]
            
            #set the requirements of salary
            if int(min_salary) >4000 and int(max_salary)>7000:
                name = link.xpath('./dt/a/text()')
                web = link.xpath('./dt/a/@href')
            
                self.f.write(str(self.count)+str(name)+"\n"+"工资："+str(min_salary)+"-"+str(max_salary)+'\n'+str(web)+'\n'+"\n")
                print('Item %d'%self.count)
                self.count += 1
        except:
            name = link.xpath('./dt/a/text()')
            web = link.xpath('./dt/a/@href')
            
            self.f.write(str(self.count)+str(name)+"（面议）"+"\n"+str(web)+'\n'+'\n')
            self.count+= 1

        
if __name__ == '__main__':
    ganji_data = ganji()
    ganji_data.load_page()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        