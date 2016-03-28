# -*- coding: utf-8 -*-
import json
from _ast import Add

import pymongo
import re
from bs4 import BeautifulSoup

mongo = pymongo.MongoClient()
db = mongo.test
collection = db.result
result = collection.find({"HasImage": True})


for r in result:
    pcontent = r['Content']
    pUrl = r['URL']
    pattern = re.compile('<img.*?src=\"(.*?)"', re.S)
    items = re.findall(pattern, pcontent)

    soup = BeautifulSoup(pcontent,"lxml")
    soupResult = soup.find_all("img")

    for i in range(0, len(items)):
        items[i] = pUrl[0:-20] + items[i]
        print items[i]
        if soupResult[i].has_attr("oldsrc"):
            del soupResult[i]["oldsrc"]
        if soupResult[i].has_attr("_fcksavedurl"):
            del soupResult[i]["_fcksavedurl"]
        if soupResult[i].has_attr("style"):
            del soupResult[i]["style"]
        if soupResult[i].has_attr("height"):
            del soupResult[i]["height"]
        if soupResult[i].has_attr("width"):
            del soupResult[i]["width"]
        soupResult[i]["src"] = items[i]

        collection.update_one({"URL": pUrl}, {'$set': {"Content": str(soup)[12:-14]}})