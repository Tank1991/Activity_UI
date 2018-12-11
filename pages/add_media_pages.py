from common.base import Base
from selenium import webdriver

class Add_media_pages(Base):

    act_name = ("xpath", "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[1]/div/div/input")

    act_mudi = ("xpath", "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[2]/div/div/div[1]/input")
    p_pai = ("xpath", "html/body/div[2]/div[1]/div[1]/ul/li[1]/span") #品牌宣传

    chexi = ("xpath", "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[3]/div/div/div[2]/input")  #推广车系
    rv80b = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[1]")
    t60 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[2]")
    mv80 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[3]")
    ev80 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[4]")
    g10 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[5]")
    v80 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[6]")
    eg10 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[7]")

    startTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[1]/div/span/../div/input")
    endTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[2]/div/span/../div/input")
    stop = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[3]/div/span")
    stopTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li31]/div/span/../div/input")

    first_source = ("xpath" ,"html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[3]/li[1]/div/span/../div/div/input")
    ziran = ("xpath" , "html/body/div[2]/div[1]/div[1]/ul/li[1]")
    def act_name_input(self , text = "活动名称信息"):
        '''
        #输入活动名称信息
        '''
        self.sendKeys(self.act_name ,text )


    def mudi(self):
        '''
        #活动目的——品牌宣传
        '''
        self.js_block()
        self.click(self.act_mudi)
        self.click(self.p_pai)
        self.js_none()

    def chexi_select(self):
        '''
        #选择车系
        '''
        self.js_block()
        self.click(self.chexi)
        self.click(self.rv80b)
        self.click(self.t60)
        self.click(self.mv80)
        self.click(self.ev80)
        self.click(self.g10)
        self.click(self.v80)
        self.click(self.eg10)
        self.click(self.stop)
        self.js_none()

    def input_time(self , statr = "2018-12-01" , end = "2018-12-05"):
        #输入开始时间 , 结束时间 ，截止时间
        self.js_block()
        self.sendKeys(self.startTime , statr)
        self.click(self.stop)
        self.sendKeys(self.endTime , end)
        self.click(self.stop)
        self.js_none()
        # self.js_block()
        # self.sendKeys(self.stopTime , stop)
        # self.js_none()

    def first_select(self ,stop = "2018-12-09"):
        '''
        选择一级来源
        '''
        self.js_block()
        self.click(self.first_source)
        # self.click(self.ziran)
        self.click(self.stop)
        self.sendKeys(self.stop ,stop)
        self.js_none()
