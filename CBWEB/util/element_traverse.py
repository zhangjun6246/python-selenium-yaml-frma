#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/6/18 17:16
# @Desc  : Description
import yaml
import os
from util.Logs import log

def  parseyaml(filename):
    """
    获取当前yaml文件的路径
    :param filename:
    :return:
    """
    #当前脚本路径的父类
    basepath=os.path.dirname(os.path.dirname(__file__))
    #类名与yaml文件要保持一致，便于取出元素
    yaml_path = basepath + "\\PageElement\\"+filename+".yaml"

    pageElements = {}
    # 遍历读取yaml文件
    with open(yaml_path, 'r', encoding='utf-8') as f:
            page = yaml.load(f)
            pageElements.update(page)
    #返回字典内容
    log.info("读取yaml成功")
    return pageElements


if __name__ == "__main__":
    a = parseyaml("login_page")
    print(a)
    print("*******************")
    print(a["username"]["type"])
    print(a["username"]["value"])
    import os
    import sys

    path = os.path.basename(sys.argv[0])[:-3]
    print(type(path))
    print(path)

