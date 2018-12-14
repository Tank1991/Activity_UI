from common.base import Base
from selenium import webdriver
from time import sleep


class Add_media_pages(Base):
    '''
    #这是媒体新增页面基础信息输入的类
    '''

    act_name = ("xpath", "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[1]/div/div/input")
    def act_name_input(self , text = "活动名称信息"):
        '''
        #输入活动名称信息
        '''
        print("输入活动名称。")
        self.sendKeys(self.act_name ,text )

    act_mudi = ("xpath", "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[2]/div/div/div[1]/input")
    p_pai = ("xpath", "html/body/div[2]/div[1]/div[1]/ul/li[1]/span") #品牌宣传
    def mudi(self):
        '''
        #活动目的——品牌宣传
        '''
        print("输入活动目的。")
        self.js_block()
        self.click(self.act_mudi)
        self.click(self.p_pai)
        self.js_none()

    chexi = ("xpath", "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[3]/div/div/div[2]/input")  #推广车系
    rv80b = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[1]")
    t60 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[2]")
    mv80 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[3]")
    ev80 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[4]")
    g10 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[5]")
    v80 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[6]")
    eg10 = ("xpath", "html/body/div[3]/div[1]/div[1]/ul/li[7]")
    def chexi_select(self):
        '''
        #选择车系
        '''
        print("选择车系。")
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

    startTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[1]/div/span/../div/input")
    endTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[2]/div/span/../div/input")
    stop = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[3]/div/span")
    stopTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[3]/div/span/../div/input")
    def input_time(self , statr = "2018-12-01" , end = "2018-12-05",stop = "2018-12-09"):
        #输入开始时间 , 结束时间 ，截止时间
        print("输入开始，结束时间。")
        self.sendKeys(self.startTime , statr)
        self.click(self.stop)
        self.sendKeys(self.endTime , end)
        self.click(self.stop)
        self.sendKeys(self.stopTime , stop)
        self.click(self.stop)

    # first_source = ("xpath" ,"html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[3]/li[1]/div/span/../div/div/input")
    first_source = ("xpath", "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[3]/li[1]/div/div/div/input")
    ziran = ("xpath" , "html/body/div[2]/div[1]/div[1]/ul/li[1]/span")
                        # html/body/div[2]/div[1]/div[1]/ul/li[1]/span
    def first_select(self):
        '''
        选择一级来源
        '''
        print("选择一级来源。")
        # self.js_block()
        js = "document.querySelectorAll('.el-scrollbar .el-select-dropdown__item')[0].click()"
        self.driver.execute_script(js)

    condition_jianshu = ("xpath" ,"html/body/div[1]/section/section/main/section/div[1]/div[2]/div/span/../div/textarea")
    def input_jianshu(self,text = "媒体新增的活动简述的哈"):
        self.sendKeys(self.condition_jianshu , text )
        self.click(self.stop)


    activity_range =  ("class name", "topText")
    def move_activity_rang(self):
        '''
        #屏幕移动到活动范围的位置
        '''
        self.huadong_now(self.activity_range)



    save = ("class name" , "save")
    def save_act(self):
        self.huadong_now(self.save)
        self.click(self.save)

