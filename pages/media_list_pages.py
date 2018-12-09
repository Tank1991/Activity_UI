from common.base import Base

class Meida_list_pages(Base):

    newActive = ("class name", "newActive")

    def click_newActive(self):
        ''''
        #点击媒体列表页面的新建按钮，进入新增页面
        '''
        self.click(self.newActive)






