from common.base import Base
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
class Select(Base):
    sleep(3)
    media  = ("xpath" , "//*[@class = 'siderbar-menu-ul']/li[1]")

    media_act = ("xpath" ,"html/body/div[1]/section/header/div/div[1]/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/span")

    def move_to_media(self):
        '''
        鼠标移动到媒体活动的方法
        :return:
        '''
        m = self.findElement(self.media)
        ActionChains(self.driver).move_to_element(m).perform()

    def click_media_act(self):
        '''
        选择媒体活动--媒体活动管理的方法
        调用鼠标移动到媒体活动的方法
        '''
        self.move_to_media()
        self.click(self.media_act)


