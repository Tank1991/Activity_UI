from common.base import Base

class LoginPage(Base):
    #定位登录
    cha = ("class name" ,"close-button")
    user = ("css selector","[class='el-input__inner'][placeholder='账号']")
    pwd = ("css selector","[class='el-input__inner'][placeholder='密码']")
    yzm = ("css selector","[class='el-input__inner'][placeholder='验证码']")
    button = ("css selector","button>span")

    #四个我知道
    know1 = ("xpath" ,".//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/div[2]/img")
    know2 = ("xpath" ,".//*[@id='app']/div/div[3]/div/div[2]/div[2]/div/div[2]/img")
    know3 = ("xpath" ,".//*[@id='app']/div/div[3]/div/div[2]/div[3]/div/div[2]/img")
    know4 = ("xpath" ,".//*[@id='app']/div/div[3]/div/div[2]/div[4]/div/div[2]/img")

    #进入活动管理平台
    huodong = ("xpath" ,".//*[@id='app']/div/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[3]/a/div")

    def click_cha(self):
        self.click(self.cha)

    def input_user(self,text =""):
        self.sendKeys(self.user,text)

    def input_pwd(self , text =""):
        self.sendKeys(self.pwd,text)

    def input_yzm(self, text =" "):
        self.sendKeys(self.yzm , text)

    def click_login_button(self):
        self.click(self.button)

    def click_know(self):
        print("点击四个我知道图片。")
        self.click(self.know1)
        self.click(self.know2)
        self.click(self.know3)
        self.click(self.know4)


    def click_huodong(self):
        print("进入活动管理平台。")
        self.click(self.huodong)

if __name__ == '__main__':

    from selenium import webdriver
    from time import sleep
    url = "https://test.maxuscloud.cn/web/authcenter/index.html#/"
    driver = webdriver.Firefox()
    driver.get(url)
    login_page = LoginPage(driver)
    login_page.click_cha()
