#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/6/20 18:12
# @Desc  : Description

from selenium import webdriver
import time
from util.Logs import log


OVER_TIME = 5
BASE_URL = "https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F"


class Page(object):

    def __init__(self, driver,url):
        """
           启动浏览器
            :param url: 测试地址
            :param driver_name: 在启动时设置浏览器的类型
            :return:
         """

        self.driver = driver
        self.driver.implicitly_wait(30)
        log.info(url)
        self.driver.get(url)
        self.driver.maximize_window()

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

    def goto_url(self,url):
        """获取用户的url地址"""
        self.driver.get(url)


    def get_url(self):
        """返回浏览器的地址"""
        return BASE_URL

    def find_element(self, BY, VALUES):
        """
        这里添加了一个OVER_TIME作为查找元素的超时次数，根据系统的实际情况设置OVER_TIME的大小
        """
        for i in range(OVER_TIME):
            try:
                return self.driver.find_element(BY,VALUES)
            except Exception as e:
                print(e)

    def find_elements(self, *locater,OVER_TIME):
        """与find_element一致"""
        for i in range(OVER_TIME):
            try:
                return self.driver.find_elements(*locater)
            except Exception as e:
                print(e)

    def find_display_elements(self, elements):
        """
        查找状态为displayed的元素集合，当查找一类元素时，
        经常出现有些元素是不可见的情况，此函数屏蔽那些不可见的元素
        """
        for i in range(OVER_TIME):
            try:
                num = elements.__len__()
            except Exception as  e:
                print(e)
                time.sleep(1)
            if num >= 1:
                break
        display_element = []
        # 将可见的元素放到列表中， 并返回
        for j in range(num):
            element = elements.__getitem__(j)
            if element.is_displayed():
                display_element.append(element)
        return display_element

    def is_element(self,element):
        """判断元素是否存在,待修改"""
        if element is not None:
            return True
        else:
            return False

    def close(self):
        self.driver.close()

    def send_text(self,element,parameter):
        """输入页面元素"""
        try:
            element.clear()
            element.send_keys(parameter)
        except Exception as e:
            print(e)

    def click(self,element):
        """点击页面元素"""
        try:
            if element !=None:
                element.click()
        except Exception as e:
            print(e)

    def quit(self):
        u"""退出浏览器"""
        self.driver.quit()

    def get_attribute(self,element,type):
        u"""获取属性内容"""
        attribut=element.get_attribute(type)
        return  attribut
    def  get_text(self,element):
        u"""获取text"""
        return element.text
    def jump_url(self,url):
        u"""跳转到指定的URl"""
        self.driver.get(url)

    '''
      def __new__(cls, *args, **kw):
          """
          使用单例模式将类设置为运行时只有一个实例，在其他Python类中使用基类时，
          可以创建多个对象，保证所有的对象都是基于一个浏览器
          """

          if not hasattr(cls, '_instance'):
              orig = super(Driver, cls)
              cls._instance = orig.__new__(cls, *args, **kw)
          return cls._instance

      '''
if __name__ == "__main__":
    page = Page()
    page.start()
