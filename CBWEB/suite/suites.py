import unittest, time, os
from util import BSTestRunner
from BeautifulReport import BeautifulReport
#path = os.getcwd()
#case_path = path + '\\case'

case_path="F:/googleDownloads/CBWEB/suite"
''' 
def create_report():
   
    test_suit = unittest.TestSuite()
    #loading所有的测试方法
    discover = unittest.defaultTestLoader.discover(case_path, pattern='test_*.py', top_level_dir=None)
    for test in discover:
        for test_case in test:
            print(test_case)
            test_suit.addTest(test_case)
    now = time.strftime('%Y-%m-%d_%H_%M', time.localtime(time.time()))
    report_dir = path + '\\report\\%s.html' % now
    print(report_dir)
    re_open = open(report_dir, 'wb')
    runner = BSTestRunner.BSTestRunner(stream=re_open, title="", description=description)
    runner.run(test_suit)
    from BeautifulReport import BeautifulReport
    result = BeautifulReport(discover)
    result.report(filename='测试报告', description='测试deafult报告', log_path='report')


create_report()
'''
def show_report():
    test_suit=unittest.TestSuite()
    case_path = "F:/googleDownloads/CBWEB/suite/case/"
    suite_tests = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py", top_level_dir=None)  # "."表示当前目录，"*tests.py"匹配当前目录下所有tests.py结尾的用例
    #添加运行
    for suites in  suite_tests:
        for suite in suites:
            test_suit.addTest(suite)
    
    BeautifulReport(suite_tests).report(filename='百度测试报告', description='张君测试',
                                        log_path='.')  # log_path='.'把report放到当前目录下


def  add_case():
    suite_tests = unittest.defaultTestLoader.discover(case_path, pattern="test_*.py", top_level_dir=None)
    return suite_tests

def run(suite):
    result=BeautifulReport(suite)
    result.report(filename='运行测试报告', description='张君测试',
                                        log_path=case_path)


if __name__=="__main__":
    case=add_case()
    for i  in case:
        print(i)
        run(i)
