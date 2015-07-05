#!/usr/bin/env python
#coding=utf-8

'''

    @date:   2015/07/04
    @name:   段家公子
    @desc:   test requests, urllib, urllib2

'''

import requests
import urllib
import urllib2


def requests_test():
    url = 'http://m.sohu.com' 
    url = 'http://m.sohu.com/?v=3&_once_=000025_v2tov3&_smuid=ICvXXapq5EfTpQTVq6Tpz'
    resp = requests.get(url)
    print resp.headers['content-type']
    page = resp.text
    
    f = open('request_index.html', 'w')
    print type(page)
    f.write(page.encode('utf8'))
    

def urllib_test():
    url = 'http://m.sohu.com/?v=3&_once_=000025_v2tov3&_smuid=ICvXXapq5EfTpQTVq6Tpz'
    resp = urllib.urlopen(url)
    '''
    print resp.getcode()
    print 'aaa'
    print resp.geturl()
    print 'aaa'
    print resp.info()
    print 'aaa'
    print resp.headers
    '''
    page = resp.read()
    f = open('./urllib_index.html', 'w')
    print type(page)
    f.write(page)
    print dir(resp)

def urllib_test2():
    s = urllib.quote('This is python')
    print 'quote:\t'+s
    s_un = urllib.unquote(s)
    print 'unquote:\t'+s_un
    s_plus = urllib.quote_plus('This is python')
    print 'quote_plus:\t'+s_plus
    s_unplus = urllib.unquote_plus(s_plus)
    print 's_unplus:\t'+s_unplus
    s_dict = {'name': 'dkf', 'pass': '1234'}
    s_encode = urllib.urlencode(s_dict)
    print 's_encode:\t'+s_encode
    print dir(urllib)


def Schedule(a, b, c):
    '''
    a:已经下载的数据快 
    b:数据块的大小
    c:远程文件的大小
    '''
    per  = 100.0*a*b/c
    if per>100:
        per = 100
    print '%.2f'%per


def urllib_test3():
    url = 'http://m.sohu.com/?v=3&_once_=000025_v2tov3&_smuid=ICvXXapq5EfTpQTVq6Tpz'
    #urllib.urlretrieve(url, './retrieve_index.html')
    url = 'http://fastlnmp.googlecode.com/files/eaccelerator-0.9.6.tar.bz2' 
    local_name = url.split('/')[-1]
    urllib.urlretrieve(url, local_name, Schedule)
        
    #print type(page), dir(page)


def urllib2_test4():
    url = 'http://m.sohu.com/?v=3&_once_=000025_v2tov3&_smuid=ICvXXapq5EfTpQTVq6Tpz'
    resp = urllib2.urlopen(url)
    page = resp.read()
    
    f = open('./urllib2_index.html', 'w')
    f.write(page)
    print dir(resp)
if __name__ == '__main__':
    #requests_test()
    #urllib_test()
    #urllib_test2()
    #urllib_test3()
    urllib2_test4()


