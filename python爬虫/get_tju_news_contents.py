# -*- coding: utf-8 -*-
import re
import urllib2
from bs4 import BeautifulSoup
import pymongo
import time
from multiprocessing.dummy import Pool as ThreadPool



def writeURL(resultDict, kind ):
    print resultDict['Title']
    print resultDict['URL']
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36'}
        request = urllib2.Request(resultDict['URL'], headers=headers)
        response = urllib2.urlopen(request)
        html = response.read().decode('utf-8')
        soup = BeautifulSoup(html, "lxml")
        content = soup.find_all("section", attrs={"class": "fck"})
        patterns = re.compile('<p.*?>(.*?)</p>', re.S)
        items = re.findall(patterns, str(content[0]))
        contentResult = ""
        for i in items:
            contentResult = contentResult + "<p>" + i.replace('<span>', '').replace('</span>', '') + "</p>"
        hasImage = re.search("img", str(content[0]))
        if hasImage:
            contentList.append(
                {'Kind': kind, 'URL': resultDict['URL'], 'Title': resultDict["Title"], 'Content': contentResult,
                 'Time': resultDict["Time"], 'HasImage': True})
        else:
            contentList.append(
                {'Kind': kind, 'URL': resultDict["URL"], 'Title': resultDict["Title"], 'Content': contentResult,
                 'Time': resultDict["Time"], 'HasImage': False})
        time.sleep(10)

    except urllib2.URLError,e:
        if hasattr(e, "code"):
            print e.code
        if hasattr(e, "reason"):
            print e.reason

if __name__ == '__main__':
    contentList = []
    mongo = pymongo.MongoClient()
    db = mongo.test
    collection = db.TZ
    #MT,RW,WH,GD,ZX，TZ
    resultCollection = db.result
    result = collection.find()
    resultList = []
    kindList = []
    num = 0
    for r in result:
        num += 1
        del r["_id"]
        writeURL(r,'TZ')
        if num%20 == 0:
            resultCollection.insert_many(contentList)
            contentList = []

    resultCollection.insert_many(contentList)
