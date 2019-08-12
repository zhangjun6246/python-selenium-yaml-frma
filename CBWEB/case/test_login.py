#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/6/20 20:32
# @Desc  : Description
import  unittest

import ddt
from selenium import webdriver
from PageObject.login_page import CBLogin
import unittest
from BeautifulReport import BeautifulReport
from util.BasePage import  Page
from util.Logs import log
from util.HandleYaml import HandleYmal
from  util.PubMethod import screedshot
import datetime
import time
import os

#获取上一级目录
root_dir=os.path.abspath(os.path.join(os.getcwd(),".."))
print(root_dir)
path=root_dir+"/config/base.yaml"
now=datetime.datetime.now().strftime('%Y-%m-%d %H_%M_%S')

@ddt.ddt
class loginTestPage(unittest.TestCase):
    img_path = 'img'
    def save_img(self, img_name):
        """
        图片的截图
        :param image:
        :return:

        """

        '''
        log.info("********************")
        root_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
        log.info(root_dir)
        img_path = root_dir + '\img'
        log.info(img_path)
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(img_path), img_name))
        '''
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))
    @classmethod
    def setUpClass(cls):
        """前置应该是读取所有内容"""

        yaml=HandleYmal()
        cls.kwargs=yaml.get_data()['testenvironment']
        cls.driver = webdriver.Chrome()
        cls.page = Page(cls.driver, cls.kwargs.get('login_url'))
        cls.loginPage = CBLogin(cls.driver)


    def zhangtestlogin(self):
        u'''
       "输入邮件账号、用户名、密码符合要求
       勾选同意协议"	1、注册成功，跳转到注册成功页面	"
        1、验证URL，https://www.chinabrands.com/site/register-success.html
        2、邮箱收到注册成功邮件
        3、数据库中user表中有成功添加注册账号数据"

        :return:
        '''
        log.info(self.kwargs)
        self.page.send_text(self.loginPage.login_sendkes_username(),self.kwargs.get('username'))
        self.page.send_text(self.loginPage.login_sendkes_password(),self.kwargs.get('password'))
        self.page.click(self.loginPage.login_click_btn())
        # 断言登录是否成功
        self.assertIsNotNone(self.loginPage.is_success(), "元素没有查找到，登录失败")

    @BeautifulReport.add_test_img("testisSucced")
    def testisSucced(self):
        u'''
        在重新加载url
        :return:
        '''
        self.page.jump_url(self.kwargs.get('login_url'))
        self.assertIsNone("notnull")
        time.sleep(3)
        log.info("没有问题")

    @BeautifulReport.add_test_img("testEroor")
    def testEroor(self):
        u"""
        执行方法为错误
        :return:
        """
        self.page.jump_url(self.kwargs.get('shooping_url'))
        log.info("执行一个截图")
        self.save_img("截图拉")
        self.assertIsNone("zhang")
        #self.page.click(self.loginPage.login_click_btn())

    '''
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    '''


if __name__=='__main__':
    #unittest.main()

    suite_tests = unittest.defaultTestLoader.discover(".", pattern="test_login.py",
                                                      top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    report_dir=root_dir+'/report'

    filename='测试报告'+now
    BeautifulReport(suite_tests).report(filename=filename, description='张君测试',
                                        log_path=report_dir)  # log_path='.'把report放到当前目录下
