# -*- coding: utf-8 -*-
import pymongo
import urllib2
import os
import sys
import time
import re


user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }
initialurl = 'http://news.tju.edu.cn/%s/index%s.htm'
mongo = pymongo.MongoClient()
db = mongo.test
ziXun = db.ZX
wenHua = db.WH
guanDian = db.GD
renWu = db.RW
meiTi = db.MT
tongZhi = db.TZ


class TJUURL:
    def __init__(self, baseURL):
        self.baseURL = baseURL
    def writeCommonURL(self,catalog, index,urlPlus,mongoCollection,split):
        rw = []
        collection = mongoCollection
        URL = self.baseURL % (catalog,index)
        print URL
        try:
            request = urllib2.Request(URL,headers = headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            pattern = re.compile('<hgroup>.*?<h4>.*?<a href="(.*?)".*?target.*?>(.*?)</a>.*?</h4>' +
                                 '.*?<h5>.*?<span>.*?</span>(.*?)</h5>.*?</hgroup>',re.S)
            items = re.findall(pattern,content)
            for item in items:
                if item[0][0:split+1] == './':
                    rw.append({"URL":"http://news.tju.edu.cn/" + urlPlus + item[0][split:],"Title":item[1],"Time":item[2]})
            collection.insert_many(rw)
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason


    def writeTZURL(self,index):
        tz = []
        catalog = "tz"
        collection = tongZhi
        URL = self.baseURL % (catalog,index)
        print URL
        try:
            request = urllib2.Request(URL,headers = headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            pattern = re.compile('<h4>.*?<a href="(.*?)".*?target.*?>(.*?)</a>.*?</h4>' +
                                 '.*?<h5>(.*?)</h5>.*?<a href',re.S)
            items = re.findall(pattern,content)
            for item in items:
                if item[0][0:2] == './':
                    tz.append({"URL":"http://news.tju.edu.cn/tz" + item[0][1:],"Title":item[1],"Time":item[2]})
            collection.insert_many(tz)
        except urllib2.URLError,e:
            if hasattr(e,"code"):
                print e.code
            if hasattr(e,"reason"):
                print e.reason



tjunews = TJUURL(initialurl)
'''
tjunews.writeCommonURL("rw","","rw",renWu,1)
tjunews.writeCommonURL("rw","_1","rw",renWu,1)
tjunews.writeCommonURL("rw","_2","rw",renWu,1)

time.sleep(15)
tjunews.writeTZURL("")
for i in range(1,17):
    temp = "_" + str(i)
    tjunews.writeTZURL(temp)
    time.sleep(15)

tjunews.writeCommonURL("zx/qb","","zx",ziXun,2)
for i in range(1,100):
    temp = "_" + str(i)
    tjunews.writeCommonURL("zx/qb",temp,"zx",ziXun,2)
    time.sleep(5)
'''
tjunews.writeCommonURL("wh","","wh",wenHua,1)
tjunews.writeCommonURL("wh","_1","wh",wenHua,1)
time.sleep(15)

tjunews.writeCommonURL("gd","","gd",guanDian,1)
tjunews.writeCommonURL("gd","_1","gd",guanDian,1)
time.sleep(15)

tjunews.writeCommonURL("mt","","mt",meiTi,1)
for i in range(1,79):
    temp = "_" + str(i)
    tjunews.writeCommonURL("mt",temp,"mt",meiTi,1)
    time.sleep(5)

