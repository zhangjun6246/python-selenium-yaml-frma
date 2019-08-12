#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/6/17 11:07
# @Desc  : Description

import unittest
import os
from selenium import webdriver
import time
import HTMLTestRunner

from selenium.webdriver.common.by import By
import sys
import importlib
importlib.reload(sys)



class CBLoginCase(unittest.TestCase):

    '''
    CB登录测试
    '''
    def setUp(self):
        self.browser = webdriver.Chrome()
        log.info("1234")

    def testPageTitle(self):
        input=(By.XPATH,u"//input[@class='custom-text']")
        self.browser.get('https://www.chinabrands.com/site/login.html?rel=/site/login.html/')
        self.browser.find_element("xpath","//input[@class='custom-text']").send_keys("1249413047@qq.com")
        #self.browser.find_element_by_xpath("//input[@class='custom-text']").send_keys("1249413047@qq.com")
        #self.browser.find_element_by_xpath("//input[@class='custom-text password']").send_keys("mm245989541")
        #self.browser.find_element_by_xpath("//button[@type='submit']").click()
        log.info("111")
        log.warning("222")
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录

    def testPrint(self):
        print("123456")

    #def tearDown(self):
    #    self.browser.quit()

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit=unittest.TestSuite()
    testunit.addTest(CBLoginCase('testPageTitle'))
    #固定路径
    HtmlFile = "F:\\googleDownloads\\CBWEB\\report\\" + now + ".html"
    print(HtmlFile)
    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(HtmlFile, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=u'CB登录测试', description='CB自动化测试')
        runner.run(testunit)
    # 关闭report，脚本结束
    report.close()

