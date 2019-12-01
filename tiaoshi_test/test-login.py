#coding:utf-8
from selenium import webdriver
from time import sleep
from case.test_case.test_login_pages import login
from case.test_case.test_add_media_pages import add_media
from selenium.webdriver.common.action_chains import ActionChains
# from case.test_case.test_media_add import media_add_jichu
from pages.select_act_pages import Select

#火狐的加载缓存信息
# profile_directory = r"C:\Users\11735\AppData\Roaming\Mozilla\Firefox\Profiles\c3h7won1.default"
# profile = webdriver.FirefoxProfile(profile_directory)
#谷歌加载
# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir= C:\\Users\\11735\\AppData\\Local\\Google\\Chrome\\User_Data')

url = "http://test102.maxuscloud.cn/web/authcenter/index.html#/"
driver = webdriver.Firefox()
login(driver, url)
add_media(driver)



# driver.find_element_by_css_selector("[class='el-input__inner'][placeholder='账号']").send_keys("15250276275")
# driver.find_element_by_css_selector("[class='el-input__inner'][placeholder='密码']").send_keys("Pass1234")




