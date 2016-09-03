# -*- coding: utf-8 -*-
"""
Created on Fri Jul 29 08:12:24 2016
图形界面

@author: pandas
"""

from process_information import pro_info
from tkinter import *
import tkinter.messagebox

class Application(Frame,pro_info):    
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        pro_info.__init__(self)
        self.grid()
        self.createWidgets()
 
    def createWidgets(self):
        Label(self, text='网址:').grid(row=0)
        Label(self, text='内容:').grid(row=1)
        self.website_ = Entry(self)
        self.website_.grid(row=0,column=1)
        self.keyword_ = Entry(self)
        self.keyword_.grid(row=1,column=1)
        self.alertButton = Button(self, text='查询', command=self.do_findMessage)
        self.alertButton.  grid(row=2,column=1)            
    
    def do_findMessage(self):
        website_w = self.website_.get()
        keyword_w = self.keyword_.get()
        self.spider_API(website_w,keyword_w)