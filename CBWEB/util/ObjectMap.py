#encoding=utf-8
#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait
from util.element_traverse import parseyaml
from util.Logs import log


# 获取单个页面元素对象
def getElement(driver, path,locatname):
    locator = parseyaml(path)
    try:
        element = WebDriverWait(driver, 5).until\
            (lambda x: x.find_element(locator[locatname]['type'],locator[locatname]['value']))
        log.info("查找元素成功，查找方式为%s    " %locator[locatname]['type'] +" 值为:%s     "% locator[locatname]['value'])
        return element
    except Exception as e:
        raise e

# 获取多个相同页面元素对象，以list返回
def getElements(driver, path, locatname):
    locator = parseyaml(path)
    try:
        elements = WebDriverWait(driver, 5).until\
            (lambda x:x.find_elements(locator[locatname]['type'],locator[locatname]['value']))
        return elements
    except Exception as e:
        raise e

if __name__ == '__main__':
    from selenium import webdriver
    # 进行单元测试
    driver = webdriver.Firefox(executable_path="e:\geckodriver.exe")
    driver.get("http://mail.126.com")
    searchBox = getElement(driver, "xpath", "//input[@name='email']")
    driver.quit()