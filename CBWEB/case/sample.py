"""
@Version: 1.0
@Project: BeautyReport
@Author: Raymond
@Data: 2017/11/17 下午3:48
@File: sample.py
@License: MIT
"""
import unittest
from BeautifulReport import BeautifulReport

if __name__ == '__main__':
    test_suite = unittest.defaultTestLoader.discover('.', pattern='test_make_report.py', top_level_dir=None)
    result = BeautifulReport(test_suite)
    result.report(filename='测试报告1', description='测试deafult报告', log_path='.')
