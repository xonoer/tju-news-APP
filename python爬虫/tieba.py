# -*- coding: utf-8 -*-
import urllib
import urllib2
import re
import scrapy
from bs4 import BeautifulSoup
import numpy
import image

class BDTB:

    def __init__(self,baseURL,pageNum):
        self.url = baseURL + '?pn=' + str(pageNum)
        self.request = urllib2.Request(self.url)
        self.content = urllib2.urlopen(self.request).read().decode('utf-8')
    def getTitle(self):
        pattern = re.compile('<h3.*?class="core_title_txt pull-left text-overflow.*?>(.*?)</h3>', re.S)
        result = re.search(pattern,self.content)
        if result:
            return result.group(1).strip()
        else:
            return None
    def getPageNum(self):
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern,self.content)
        if result:
            return result.group(1).strip()
        else:
            return None


baseURL = 'http://tieba.baidu.com/p/3138733512'
bdtb = BDTB(baseURL,1)
print bdtb.getPageNum()
print bdtb.getTitle()
