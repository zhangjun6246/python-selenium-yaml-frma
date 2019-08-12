#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/7/8 17:22
# @Desc  : Description
import yaml
import os

class HandleYmal:
    """
    获取测试环境的配置
    """
    def __init__(self,file_path=None):
        if file_path:
            self.file_path=file_path
        else:
            #获取path
            root_dir=os.path.dirname(os.path.abspath('.'))
            print(root_dir)
            self.file_path=root_dir+"/config/base.yaml"
    def get_data(self):
        fp=open(self.file_path,encoding="utf-8")
        data=yaml.load(fp)
        return  data


if __name__ == '__main__':
    test=HandleYmal()
    p=test.get_data()
    print(p['testenvironment'])


