# coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

class Base():
    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.poll = 0.5

    def findElement(self, loctor ):
            # '''
            # :param self:
            # :param loctor:
            # :return:
            # args:
            # loctor 传元祖，如（"id","xx")
            #方法：通过by查找元素
        # "id"，"xpath"，"link text"，"partial link text"，"name"，"tag name"，"class name"，"css selector"
            # '''
        element = WebDriverWait(self.driver, self.timeout, self.poll).until(lambda x:
    x.find_element(*loctor))
        # print("正在定位元素:方法是-->%s,   value值是-->%s"%(loctor[0]  ,loctor[1]))
        return element

    def click(self, loctor):
        ele = self.findElement(loctor)
        ele.click()

    def sendKeys(self, loctor, text, is_clear_first=False):
        '''
        给元素传值
        loctor 传元素的元祖，如（"id","xx")
        text:是输入的值
        is_clear_first默认为False，不清空输入框
        '''
        ele = self.findElement(loctor)
        if is_clear_first:
                ele.clear() # is_clear_first 为True的时候执行
        ele.send_keys(text)
        print("正在定位元素:方法是-->%s,  value值是-->%s， 传的值是-->%s"%  (loctor[0],loctor[1],text))

    def isSelected(self,locator):
        '''
        locator：元素的定位对象
        判断元素是否被选中，返回bool值
        '''
        ele = self.findElement(locator)
        r = ele.is_selected()
        return  r

    def isElementExist(self,locator):
        '''单个元素判断是否存在'''
        try:
            ele = self.findElement(locator)
            return True
        except:
            return False

    def isElementExits(self,locator):
        '''多个元素判定存在'''
        eles = self.findElement(locator)
        n =len(eles)
        if n == 0:
            return False
        elif n == 1 :
            return True
        else:
            print("定位到多个元素%s"%n)
        return True

    def huadong_down(self):
        '''
        向下滑动屏幕
        '''
        # js = "window.scrollTo(0,10000);"
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)

    def huadong_up(self):
        '''
        向上滑动屏幕
        '''
        js = "window.scrollTo(0,0);"
        self.driver.execute_script(js)

    def huadong_now(self,locator):
        '''
        滚动到元素的位置
        '''
        target  = self.findElement(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();",target )

    def switch_to_frame(self,id_name_index= '',locator= ''):
        '''
        方法：切换到iframe页面，只可以传一个值
        id_name_index:传的是frame的id/name/index属性
        locator：传的是frame的元素对象
        '''
        if locator == '':
            self.driver.switch_to.frame(id_name_index)
            # print("这是frame的id/name/index属性。")
        elif id_name_index == '':
            self.driver.switch_to.frame(self.findElement(locator))
            # print("这是frame的对象。")
        else:
            print("请输入有效的iframe对象属性！")

    def select(self,locator,index='',value='',text=''):
        '''
        方法：下拉框传值
        locator：是下拉框对象
        value：对应option的value值
        index：第几个
        text：对应option的text值
        '''
        if value != '':
            Select(self.findElement(locator)).select_by_value(value)
            # print("value属性。")
        elif index != '':
            Select(self.findElement(locator)).select_by_index(index)
        elif text != '':
            Select(self.findElement(locator)).select_by_visible_text(text)
            # print("text属性。")
        else:
            print("请输入对应的下拉框属性！")

    def mouse_move(self,locator):
        '''
        方法：鼠标悬停到某个元素
        locator：要悬停的元素对象
        '''
        ActionChains(self.driver).move_to_element(self.findElement(locator)).perform()

    def alert_accept(self):
        '''
        方法：弹出框警告框处理，打印出文本信息
        '''
        a = self.driver.switch_to.alert()
        print(a.text())
        a.accept()

    def js_block(self):
        for i in range(1):
            js = 'document.getElementsByClassName("el-select-dropdown el-popper")[%s].style.display= "block"'%i
            self.driver.execute_script(js)


    def js_none(self):
        for i in range(1):
            js = 'document.getElementsByClassName("el-select-dropdown el-popper")[%s].style.display= "none"'%i
            self.driver.execute_script(js)

