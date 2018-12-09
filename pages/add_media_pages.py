from common.base import Base

class Add_media_pages(Base):

    act_name = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[1]/div/div/input")

    act_mudi = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[2]/div/div/div[1]/input")
    p_pai = ("xpath" , "html/body/div[2]/div[1]/div[1]/ul/li[1]/span") #品牌宣传

    chexi = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[3]/div/div/div[2]/input")  #推广车系
    rv80b = ("xpath" , "html/body/div[3]/div[1]/div[1]/ul/li[1]")
    t60 = ("xpath" , "html/body/div[3]/div[1]/div[1]/ul/li[2]")
    mv80 = ("xpath" , "html/body/div[3]/div[1]/div[1]/ul/li[3]")
    ev80 = ("xpath" , "html/body/div[3]/div[1]/div[1]/ul/li[4]")
    g10 = ("xpath" , "html/body/div[3]/div[1]/div[1]/ul/li[5]")
    v80 = ("xpath" , "html/body/div[3]/div[1]/div[1]/ul/li[6]")
    eg10 = ("xpath" , "html/body/div[3]/div[1]/div[1]/ul/li[7]")

    startTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[1]/div/span/../div/input")
    endTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[2]/div/span/../div/input")
    stopTime = ("xpath" , "html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li31]/div/span/../div/input")

    first_source = ("xpath" ,"html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[3]/li[1]/div/span/../div/div/input")

    def act_name_input(self , text = "1234"):
        '''
        #输入活动名称信息
        '''
        self.sendKeys(self.act_name ,text )

    def mudi(self):
        '''
        #活动目的——品牌宣传
        '''
        self.click(self.act_mudi)
        self.click(self.p_pai)

    def chexi_select(self):
        '''
        #选择车系
        '''
        self.click(self.chexi)
        self.click(self.rv80b)
        self.click(self.t60)
        self.click(self.mv80)
        self.click(self.ev80)
        self.click(self.g10)
        self.click(self.v80)
        self.click(self.eg10)

    def input_time(self , statr = "2018-12-01" , end = "2018-12-05" ,stop = "2018-12-09"):
        #输入开始时间 , 结束时间 ，截止时间
        self.sendKeys(self.startTime , statr)
        self.sendKeys(self.endTime , end)
        self.sendKeys(self.stopTime , stop)

    def first_select(self):
        self.click(self.first_source)







