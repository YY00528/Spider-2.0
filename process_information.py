# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 07:59:44 2016
抓取信息

@author: pandas
"""

from getURL import getURL_website
import urllib.request

class pro_info(getURL_website):
    dict_choose = {}#层数对比
    dict_M = []
    list_W = []
    webUrl = set()
    
    def __init__(self):
        getURL_website.__init__(self)
            
    def urlJudge(self,url):#运用list去重
        if url not in self.dict_M:
            self.dict_M.append(url)
            return True
        else:
            return False
            
    '''
    def urlSet(self,site):#集合去重,与list去重任选一种
        if site not in self.webUrl:
            self.webUrl |= {site}
            return True
        else:
            return False
        
    def saveFile(self,web):
        file = open('TEST'+str(self.i)+'.txt','wb')
        url = urllib.request.urlopen(web)
        buf = url.read()
        file.write(buf)
        file.close()
        self.i += 1
      
    ''' 
    def PrintMessage(self,lines,website):
        #self.saveFile(website)
        '''#######################补全网址######################'''
        if website[0:5]!='http:' and website[0:2]=='//':
            ws = 'http:'+website
        elif website[0:5]!='http:' and website[0:2]!='//':
            ws = 'http://'+website
        else:
            ws = website
        
        if not self.dict_choose:
            self.dict_choose[ws] = 0
        self.urlJudge(ws)#list去重
        
        '''########################当前网页中的所有网址###########'''
        for link in lines:
            if 'href'in link.attrs:#判断能否进行深度搜索
                if link['href']=='/' or link['href']=='#':
                    continue
                else:
                    website_T = link['href']
                    if link['href'][0:5]=='http:':
                        if website_T not in self.dict_choose.keys():
                            self.dict_choose[website_T] = self.dict_choose[ws]+1
                            num = self.dict_choose[website_T]
                            num = self.dict_choose[website_T]
                            self.BFS_control(website_T,num)
                    elif link['href'][0:2]=='//':
                        website_T = 'http:'+website_T
                        if website_T not in self.dict_choose.keys():
                            self.dict_choose[website_T] = self.dict_choose[ws]+1
                            num = self.dict_choose[website_T]
                            num = self.dict_choose[website_T]
                            self.BFS_control(website_T,num)
                    elif link['href'][0:1]=='/':   
                        if link['href'][1:] not in ws:
                            if ws[-1:]!='/':
                                website_T = ws + '/' + website_T
                            else:
                                website_T = ws + website_T
                            if website_T not in self.dict_choose.keys():
                                self.dict_choose[website_T] = self.dict_choose[ws]+1
                                num = self.dict_choose[website_T]
                                num = self.dict_choose[website_T]
                                self.BFS_control(website_T,num)
                    elif link['href'][0:11]   == 'javascript:'   :
                        continue
                    else:
                        if website_T not in self.dict_choose.keys():
                            self.dict_choose[website_T] = self.dict_choose[ws]+1
                            num = self.dict_choose[website_T]
                            self.BFS_control(website_T,num)

    def BFS_control(self,url,judge):  #控制层数
        if judge<2:
            self.list_W.append((url,judge))

    def all_url_run(self,key_Mess):#循环抓取信息
        j = 1  
        while j<len(self.list_W):
            try:
                if self.list_W[j][0]:
                    all_urls = self.deepFind(self.list_W[j][0],key_Mess)
                    self.PrintMessage(all_urls,self.list_W[j][0])
                j += 1
            except:
                print("跳过异常")
                j += 1
    def spider_API(self,we,ke):
        if we[0:7]=='http://':
            info = self.deepFind(we,ke)
            self.BFS_control(we,0)
            self.PrintMessage(info,we)
            self.all_url_run(ke)
        else:
            info = self.deepFind('http://'+we,ke)
            self.BFS_control('http://'+we,0)
            self.PrintMessage(info,'http://'+we)
            self.all_url_run(ke)
            
            