# -*- coding: utf-8 -*-
import pymongo
import json
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


mongo = pymongo.MongoClient()
db = mongo.test
collection = db.result

result = collection.find({"Kind":"RW"})
f = open("test.json","w")
f.write("[")
for r in result:
   del r["_id"]
   jsonFile = json.dumps(r,ensure_ascii=False) + ","
   f.write(jsonFile)
   f.write("\n")
   print jsonFile
f.write("]")
f.close()


f = file("test.json")
test = json.load(f,encoding="utf-8")
print test[3]["Content"]