#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/7/2 13:37
# @Desc  : Description


import  unittest
from selenium import webdriver
from PageObject.shooping_order_page import ShoopingOrder
from BeautifulReport import BeautifulReport
from util.BasePage import  Page
from case.public_login import commonality
from util.Logs import log
from util.HandleYaml import HandleYmal
import  time
class shoopingOrder(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """前置应该是读取所有内容"""
        cls.driver = webdriver.Chrome()
        yaml = HandleYmal()
        log.info("123")
        cls.kwargs = yaml.get_data()['testenvironment']

    def testShooping(self):
        """添加商品到购物车"""
        order=ShoopingOrder(self.driver)
        page = Page(self.driver, self.kwargs.get("shooping_url"))
        attribute=page.get_attribute(order.is_login(),'title')
        # 判断元素是否已登录
        if len(str(attribute))>0:
            log.info("不用登录")
        else:
            print("需要进行登录")
            conmm=commonality()
            conmm.login(self.driver,self.kwargs.get("login_url"))
            time.sleep(5)
        #点击元素内容
        page.click(order.shooping_add_cart())
        #点击购物车按钮
        page.click(order.shooping_cart_btn())
        #获取总价
        price=page.get_text(order.get_total())
        #进行结算
        page.click(order.click_checkout())
        time.sleep(7)
        all_total=order.get_all_total()
        print(all_total)
        #计算总价
        calculate_total=0
        for total in all_total:
            total_price = page.get_attribute(total,'data-orgp')
            calculate_total=float(total_price)+calculate_total

        # 获取总价
        page_get_total=page.get_text(order.get_total_price())
        print(calculate_total)
        print(page_get_total)
        self.assertEqual(page_get_total,str(calculate_total),"页面获得价格与实际匹配的价格不一致")


if __name__=='__main__':
    unittest.main()
    ''' 
    suite_tests = unittest.defaultTestLoader.discover(".", pattern="test_shooping_order.py",
                                                      top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    BeautifulReport(suite_tests).report(filename='cb报告', description='购物车测试',
                                        log_path='.')  # log_path='.'把report放到当前目录下
    '''

