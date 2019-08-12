#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/7/2 11:46
# @Desc  : Description

from util.BasePage import Page
import os

from util.ObjectMap import getElement,getElements


class ShoopingOrder(Page):
    def __init__(self, driver):
        # 获取当前文件的名称，
        self.driver=driver
        self.path = os.path.basename(__file__)[:-3]

    def shooping_add_cart(self):
        u"""添加到购物车 """
        return getElement(self.driver, self.path, 'addCart')

    def shooping_cart_btn(self):
        u"""购物车按钮"""
        return getElement(self.driver, self.path, 'shooping')

    def check_goods(self):
        u"""点击商品"""
        return getElement(self.driver, self.path, 'checkGoods')

    def get_total(self):
        u"""获取总价"""
        return getElement(self.driver, self.path, 'getPrice')

    def click_checkout(self):
        u"""点击结算"""
        return getElement(self.driver, self.path, 'proceedCheckout')

    def is_login(self):
        return getElement(self.driver,self.path,'isLogin')

    def get_all_total(self):
        u"""获取所有单个分类的总价"""
        return getElements(self.driver, self.path, 'getTotalPrice')
    def get_total_price(self):
        return getElements(self.driver, self.path, 'totalPrice')