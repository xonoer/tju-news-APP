# -*- coding: utf-8 -*-

import pytesseract
from PIL import Image
import urllib2
import pymongo

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',}
url = "http://e.tju.edu.cn/Kaptcha.jpg"
request = urllib2.Request(url,headers = headers)
response = urllib2.urlopen(request)
ima = response.read()
f = open("code.jpg", "wb")
f.write(ima)
f.close()
image = Image.open("code.jpg")
print pytesseract.image_to_string(image)

im = Image.open("./images/0040.gif")
print type(im)
code = pytesseract.image_to_string(im)
print type(code)

mongo = pymongo.MongoClient()
db = mongo.test
test = db.test
test.insert({"hasImage":False})



