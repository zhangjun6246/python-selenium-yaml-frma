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


class CBTestCase(unittest.TestCase):
    '''
    CB登录测试
    '''
    def setUp(self):
        self.browser = webdriver.Chrome()
        #self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('http://sa.hqygou.com/')
        self.browser.find_element_by_xpath("//input[@name='username']").send_keys("zhangjun1")
        self.browser.find_element_by_xpath("//input[@name='password']").send_keys("zhangjun1")
        self.browser.find_element_by_xpath("//input[@name='dosubmit']").click()
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        # 必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path = 'F:\\googleDownloads\\CBWEB\\report\\' + now + '.png'
        print(pic_path)
        self.browser.save_screenshot(pic_path)
    def testPrint(self):
        print("123456")

    def tearDown(self):
        self.browser.quit()

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit=unittest.TestSuite()
    testunit.addTest(CBTestCase('testPageTitle'))
    HtmlFile = "F:\\googleDownloads\\CBWEB\\report\\" + now + ".html"
    print(HtmlFile)
    # 将运行结果保存到report，名字为定义的路径和文件名，运行脚本
    with open(HtmlFile, 'wb') as report:
        runner = HTMLTestRunner.HTMLTestRunner(stream=report, title=u'DEMO测试', description='修改html报告')
        runner.run(testunit)
    # 关闭report，脚本结束
    report.close()

