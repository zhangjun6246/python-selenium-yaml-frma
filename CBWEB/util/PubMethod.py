#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/7/15 11:27
# @Desc  : Description
import os

def screedshot(driver,test_method):
    """
    图片的截图
    :param image:
    :return:

    """

    root_dir=os.path.abspath(os.path.join(os.getcwd(),".."))
    img_path=root_dir+'/report/screenshot'
    driver.get_screenshot_as_file('{}/{}.png'.format(img_path,test_method))