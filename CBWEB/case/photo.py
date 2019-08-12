#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/7/16 18:23
# @Desc  : Description

import unittest,time,os
from selenium import webdriver
from BeautifulReport import BeautifulReport
root_dir=os.path.abspath(os.path.join(os.getcwd(),".."))
class Test_01(unittest.TestCase):
    def save_img(self, img_name):  #错误截图方法，这个必须先定义好
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        root_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
        img_path = root_dir + '\img'
        self.driver.get_screenshot_as_file('{}/{}.png'.format(img_path, img_name))    #os.path.abspath(r"G:\Test_Project\img")截图存放路径
    def setUp(self):
        print("开始测试")
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.baidu.com/")
    def tearDown(self):
        print("结束测试")
        self.driver.close()
    def test_case_1(self):
        time.sleep(3)
        text_data=self.driver.find_element_by_xpath('//div[@id="u1"]/a').text
        self.assertEqual("新闻",text_data)
    @BeautifulReport.add_test_img('test_case_2')     #截图装饰器，当你用例错误了，那么会自动调用save_img截图方法，存到指定目录下
    def test_case_2(self):
        time.sleep(3)
        text_data = self.driver.find_element_by_xpath('//div[@id="u1"]/a').text
        self.assertEqual("新闻1", text_data)

import unittest,time,os
from BeautifulReport import BeautifulReport
current_path = os.getcwd()
report_path = os.path.join(current_path, "Report")
now = time.strftime('%Y-%m-%d_%H_%M_%S')
# 报告地址&名称
#report_title = 'Example报告' + now + ".html"  # 如果不能打开这个文件，可能是now的格式，不支持：和空格
if __name__ == '__main__':
    ''' 
    suite = unittest.TestSuite()
    loader=unittest.TestLoader()
    suite.addTests(loader.loadTestsFromModule(photo))
    #运行用例filename=报告名称，description=所有用例总的名称，log_path=报告路径,如果不填写默认当前目录
    BeautifulReport(suite).report(filename="测试报告", description ='Test_01模块', log_path =report_path)
    '''
    suite_tests = unittest.defaultTestLoader.discover(".", pattern="photo.py",
                                                      top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例

    report_dir = root_dir + '/report'

    filename = '测试报告' + now
    BeautifulReport(suite_tests).report(filename=filename, description='张君测试',
                                        log_path="F:\\googleDownloads\\CBWEB\\report")  # log_path='.'把report放到当前目录下