#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: zhangjun
# @Date  : 2019/6/17 18:51
# @Desc  : Description


import logging
import logging.handlers
import os
import time

def logs():
        logger = logging.getLogger("")
        # 设置输出的等级
        LEVELS = {'NOSET': logging.NOTSET,
                  'DEBUG': logging.DEBUG,
                  'INFO': logging.INFO,
                  'WARNING': logging.WARNING,
                  'ERROR': logging.ERROR,
                  'CRITICAL': logging.CRITICAL}
        # 创建文件目录

        logs_dir = os.path.dirname(os.path.dirname(__file__)) + "\\Logs\\ALL_logs"
        if os.path.exists(logs_dir) and os.path.isdir(logs_dir):
                pass
        else:
                os.mkdir(logs_dir)
        # 修改log保存位置
        timestamp = time.strftime("%Y-%m-%d", time.localtime())
        logfilename = '%s.log' % timestamp
        logfilepath = os.path.join(logs_dir, logfilename)
        print(logfilepath)
        rotatingFileHandler = logging.handlers.RotatingFileHandler(filename=logfilepath,
                                                                   maxBytes=1024 * 1024 * 50,
                                                                   backupCount=5)
        # 设置输出格式
        formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')
        rotatingFileHandler.setFormatter(formatter)
        # 控制台句柄
        console = logging.StreamHandler()
        console.setLevel(logging.INFO)
        #console.setLevel(logging.ERROR)
        console.setFormatter(formatter)
        # 添加内容到日志句柄中
        logger.addHandler(rotatingFileHandler)
        logger.addHandler(console)
        logger.setLevel(logging.NOTSET)
        return logger

class zhangjuntest(object):
    def test_show(self):
        print("进行日志文件显示")
log = logs()



