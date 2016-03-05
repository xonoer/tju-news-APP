# -*- coding: utf-8 -*-
import urllib2
import re
from bs4 import BeautifulSoup
import time
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)\
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.118 Safari/537.36',}
url1 = 'http://jandan.net/ooxx/page-%s#comments'

urlList = []
numList = []
for i in range(1650, 1702):
    urlList.append(url1 % str(i))
    numList.append(i)

def running((url, no)):
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    html = response.read().decode('utf-8')
    soup = BeautifulSoup(html, "lxml")
    a = soup.find_all('a', attrs={'class': 'view_img_link'})
    b = 1
    for r in a:
        if str(r.get("href")).endswith('gif'):
            continue
        print "sub   %s" % str(no), r.get("href")
        try:
            request = urllib2.Request(r.get("href"), headers=headers)
            response = urllib2.urlopen(request)
            image = response.read()
            f = open("./meizi/test%4d%03d.jpg" % (no, b), "wb")
            f.write(image)
            f.close()
            b += 1
            time.sleep(15)
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
                continue
            if hasattr(e, "reason"):
                print e.reason
                continue


if __name__ == '__main__':
    pool = ThreadPool(4)
    pool.map(running, zip(urlList, numList))
    pool.close()
    pool.join()
    '''thread_list = []
    thread_list.append(MyThread(running, (10, urlList.pop(0), numList.pop(0))))
    thread_list.append(MyThread(running, (10, urlList.pop(0), numList.pop(0))))
    thread_list.append(MyThread(running, (10, urlList.pop(0), numList.pop(0))))
    thread_list.append(MyThread(running, (10, urlList.pop(0), numList.pop(0))))

    for k in thread_list:
        k.setDaemon(True)
        k.start()
    for l in thread_list:
        l.join()
    while True:
        print "main"
        for n in range(4):
            if not thread_list[0].isAlive():
                if len(numList) != 0:
                    thread_list.pop(0)
                    thread_list.append(MyThread(running, (5, urlList.pop(0), numList.pop(0))))
                    time.sleep(5)
        for k in thread_list:
            k.setDaemon(True)
            k.start()
        for l in thread_list:
            l.join()

    print "end"
    '''
