#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/6/15 9:11
# @Desc  : Description

from util.BasePage import Page

import os
from util.ObjectMap import *


class CBLogin(Page):

    def __init__(self,driver):
        self.driver=driver
        self.path = os.path.basename(__file__)[:-3]

    def login_click_btn2(self):
        """点击登录按钮"""
        return getElement(self.driver,self.path ,'loginbtn')
    def login_sendkes_username(self):
        """登录框输入内容"""
        return getElement(self.driver, self.path , 'username')
    def login_sendkes_password(self):
        """密码输入框"""
        return getElement(self.driver, self.path , 'password')

    def login_click_btn(self):
        """点击登录按钮"""
        return getElement(self.driver, self.path, 'loginbtn')
    def is_success(self):
        """判断是否登录成功"""
        return  getElements(self.driver,self.path,'logsuccess')


