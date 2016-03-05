# -*- coding: utf-8 -*-
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageFilter
import pymongo
import json
from bs4 import BeautifulSoup
import urllib2
import re

mongo = pymongo.MongoClient()
db = mongo.test
collection = db.MT
result = collection.find_one()
print type(str(result["URL"]))
request = urllib2.Request(result["URL"])
response = urllib2.urlopen(request)
content = response.read().decode('utf-8')
soup = BeautifulSoup(content,"lxml")
result = soup.find_all('div',attrs={"class":"Custom_UnionStyle"})
print result
for tag in result:
    print tag