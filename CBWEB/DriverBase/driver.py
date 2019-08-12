#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/7/2 17:39
# @Desc  : Description

def start(self, url=BASE_URL, driver_name="Chrome"):
    """
    启动浏览器
    :param url: 测试地址
    :param driver_name: 在启动时设置浏览器的类型
    :return:
    """
    if driver_name == "Firefox":
        self.driver = webdriver.Firefox()
    elif driver_name == "Ie":
        self.driver = webdriver.Ie()
    else:
        self.driver = webdriver.Chrome()
    self.driver.implicitly_wait(OVER_TIME)
    self.driver.get(url)
    self.driver.maximize_window()