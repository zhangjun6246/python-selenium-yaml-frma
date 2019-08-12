#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/7/3 11:47
# @Desc  : Description
from util.BasePage import  Page
from PageObject.login_page import CBLogin

class commonality(object):
    def login(self,driver,url):
        loginPage = CBLogin(driver)
        page=Page(driver,url)
        page.send_text(loginPage.login_sendkes_username(),"jun@qq.com")
        page.send_text(loginPage.login_sendkes_password(), "zhangjun1!")
        page.click(loginPage.login_click_btn())

