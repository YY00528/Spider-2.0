# -*- coding: utf-8 -*-
"""
Created on Sun 4/12 10:02:26 2016
获取网址
@author: 龙
"""

import urllib.request
from bs4 import BeautifulSoup
import re
import http.cookiejar,urllib.parse

class getURL_website(object):
    
    proxy = {1:'http://xx.xx.xx.xx:xx',2:'http://xx.xx.xx.xx:xx'}
    
    def __init__(self):
        pass
    
    def getNum(self):
        j = j+1
        return j;
    
    def getHTML(self,url):
        try:#伪装成浏览器+cookie的处理
            cj = http.cookiejar.CookieJar()
            opener = urllib.request.build_opener(\
            urllib.request.HTTPCookieProcessor(cj))
            opener.addheaders = [('User-Agent',
            'Mozilla/5.0 (Windows NT 6.1;WOW64) AppleWebKit\
            /537.36 (KHTML, like Gecko) Chrome/41.0.2272.101\
            Safari/537.36'),
            ('Cookie','4564564564564564565646540')]
            urllib.request.install_opener(opener)
            html_bytes=''
            try:
                html_bytes = urllib.request.urlopen(url).read()
                html_bytes = html_bytes.decode('utf-8')
            except:
                html_bytes = urllib.request.urlopen(url).read()
        except:#使用代理服务器
            try:
                urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler(self.proxy[1]),urllib.request.HTTPHandler))
            except:
                urllib.request.install_opener(urllib.request.build_opener(urllib.request.ProxyHandler(self.proxy[2]),urllib.request.HTTPHandler))
            html_bytes = urllib.request.urlopen(url).read().decode('utf-8')
        finally:
            return html_bytes
        
    def subMessage(self,message):
        p = re.compile(r'[(<.*> | \s | \\ | \/ | \= | {.*} | & | : | ; | \" | \' | # | \-) | (a-zA-Z)*]')
        length = len(message)
        for link in range(length):
            print('message-->{}\n'.format(p.sub('',str(message[link].contents))))
    
    def deepFind(self,websiteTest,keyword):#关键词搜索
        html_doc = self.getHTML(websiteTest)
        soup = BeautifulSoup(
                            html_doc,
                            'html.parser',#解析器
                            from_encoding='utf-8'
                            )
        some = soup.find_all(re.compile(r'[a | p]'),text=re.compile(r'[^\w]*'+keyword+r'[\w$]*'))
        self.subMessage(some)
        return some
        
        