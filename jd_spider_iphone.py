# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 16:13:34 2018

@author: 13758
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 09:42:41 2018

@author: 13758
"""

from pylab import *
import os
import sys
import requests
import matplotlib.pyplot as plt
import random
import json
import time
import urllib.request
from collections import Counter

class jd:
    def __init__(self):
        self.begin_page = 2#int(input("Begin page:"))
        self.end_page = 10#int(input("End page:"))
        self.count = 1
        self.page =0
        cwd = os.getcwd()
        if not os.path.exists(os.path.join(cwd,'TMALL_PICS')):
            os.makedirs(os.path.join(cwd,'TMALL_PICS'))
        self.pic_dirs = os.path.join(cwd, 'TMALL_PICS')
        self.year = []
        self.month = []
        self.color = []
        self.storage = []
        self.content = []
                    
    def load_page(self):
        
        print('Data Searching')
        
        for pn in range(self.begin_page-1, self.end_page):
            url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv872&productId=100002425003&score=0&sortType=5&page='+str(pn)+'&pageSize=10&isShadowSku=0&fold=1'
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

            ua = {"User-agent":random.choice(ua_list)}
            print(url)
            response = requests.get(url, headers = ua)
            html = response.text
            
            html = html.replace('fetchJSON_comment98vv872(','')
            html = html.replace(');','')
            
            j_html = json.loads(html)
            comments = j_html['comments']
    
            comment_jd = {}
        for item in comments:
            
            comment_jd['year']=item['referenceTime'].split('-')[0]
            comment_jd['month']=item['referenceTime'].split('-')[1]
            comment_jd['color']=item['productColor']
            comment_jd['storage']=item['productSales'][0]['saleValue']
            comment_jd['content'] = item['content']
            self.year.append(comment_jd['year'])
            self.month.append(comment_jd['month'])
            self.color.append(comment_jd['color'])
            self.storage.append(comment_jd['storage'])
            self.content.append(comment_jd['content'])
        
    def analyse(self):
        print('Data Analysing')
        cwd = os.getcwd()
        if not os.path.exists(os.path.join(cwd,'jd_figs')):
            os.makedirs(os.path.join(cwd,'jd_figs'))
        fig_dirs = os.path.join(cwd,'jd_figs')
        year = Counter(self.year);month = Counter(self.month);color = Counter(self.color);storage = Counter(self.storage)
        year = [(k,year[k]) for k in sorted(year.keys())] 
        month = [(k,month[k]) for k in sorted(month.keys())]
        color = [(k,color[k]) for k in sorted(color.keys())]
        storage = [(k,storage[k]) for k in sorted(storage.keys())]
        month_name = [x[0] for x in month ]
        print(month_name)
        month_value = [x[1] for x in month]
        year_name = [x[0] for x in year];
        year_value = [x[1] for x in year]
        color_name = [x[0] for x in color];
        color_value = [x[1] for x in color]
        storage_name = [x[0] for x in storage];
        storage_value = [x[1] for x in storage]

        
        mpl.rcParams['font.sans-serif'] = ['SimHei'] #指定默认字体
        mpl.rcParams['axes.unicode_minus'] = False #解决保存图像是负号'-'显示为方块的问题 
        
        plt.style.use('ggplot')
        plt.subplot(221)
        plt.bar(year_name, year_value, color = 'r', align = 'center')
        plt.subplot(222)
        plt.bar(month_name, month_value, color = 'r', align = 'center')
        plt.subplot(223)
        plt.bar(color_name,color_value, color = 'r', align = 'center')
        plt.subplot(224)
        plt.bar(storage_name,storage_value, color = 'r', align = 'center')
        plt.subplots_adjust( hspace=0.6)
        plt.savefig(os.path.join(fig_dirs,'jd_data.png'))

    def download(self,img_link):
        img_link = str(img_link)
        try:
            if img_link== '[]':
                self.count = self.count
            elif ',' in img_link:
                img_link = img_link.replace("'",'').replace('[','').replace(']','').replace('//','').replace(' ','')
                img_links = img_link.split(',')
                for item in img_links:
                    print("Downloading Pic %d" %self.count)
                    item = "http://"+item
                    with open(self.pic_dirs+"/"+str(self.count)+'.jpg','wb') as f:
                        img = urllib.request.urlopen(item).read()
                        f.write((img))
                    self.count+=1
            else:
                img_link = img_link.replace("'",'').replace('[','http:').replace(']','')
                print("Downloading Pic %d" %self.count)
                with open(self.pic_dirs+"/"+str(self.count)+'.jpg','wb') as f:
                    img = urllib.request.urlopen(img_link).read()
                    f.write((img))
                self.count+=1
        except urllib.request.HTTPError as e:
            print('Jump Error')
                
if __name__=="__main__":
    my_jd=jd()
    my_jd.load_page()
    my_jd.analyse()
    print("Finish all")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        