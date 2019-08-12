#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/8/6 11:54
# @Desc  : Description
import  unittest
from selenium import  webdriver
import  time
class Blogs(unittest.TestCase):
    '''
    打开博客园网址，记录标题页面，在找找看输入框中，输入网址的标题，模糊查询关键词：接口测试，
    查看测试结果中是否包含本次打开的网站标题
    '''

    @classmethod
    def setUp(self):
        self.brower=webdriver.Chrome()

    def testQuers(self):
        self.brower.get("https://www.cnblogs.com/chongyou/")
        title=self.brower.title
        #输入内容
        self.brower.find_element_by_id("q").send_keys(title)
        #点击
        self.brower.find_element_by_id("btnZzk").click()
        #获取网页所有的标题
        html=self.brower.page_source
        print(html)

if __name__ == '__main__':
    time.strftime("")
