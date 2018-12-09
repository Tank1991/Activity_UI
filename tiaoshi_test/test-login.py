#coding:utf-8
from selenium import webdriver
from time import sleep
from case.test_case.test_login_pages import login
from selenium.webdriver.common.action_chains import ActionChains

from pages.select_act_pages import Select

#火狐的加载缓存信息
# profile_directory = r"C:\Users\11735\AppData\Roaming\Mozilla\Firefox\Profiles\c3h7won1.default"
# profile = webdriver.FirefoxProfile(profile_directory)
#谷歌加载
# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir= C:\\Users\\11735\\AppData\\Local\\Google\\Chrome\\User_Data')

url = "https://test102.maxuscloud.cn/web/authcenter/index.html#/"
driver = webdriver.Firefox()
login(driver, url)
# driver.maximize_window()
# driver.get(url)
# try:
#     driver.find_element_by_class_name("close-button").click()
# except:
#     pass
# driver.find_element_by_css_selector("[class='el-input__inner'][placeholder='账号']").send_keys("15250276275")
# driver.find_element_by_css_selector("[class='el-input__inner'][placeholder='密码']").send_keys("Pass1234")
# driver.find_element_by_css_selector("[class='el-input__inner'][placeholder='验证码']").send_keys(" ")
# driver.find_element_by_css_selector("button>span").click()
# sleep(3)
# driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div/div[2]/div[1]/div/div[2]/img").click()
# driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div/div[2]/div[2]/div/div[2]/img").click()
# driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div/div[2]/div[3]/div/div[2]/img").click()
# driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div/div[2]/div[4]/div/div[2]/img").click()
#进入活动管理平台
# driver.find_element_by_xpath(".//*[@id='app']/div/div[3]/div/div[3]/div/div[1]/div[2]/div[2]/ul/li[3]/a/div").click()

# move_media = Select(driver)
# move_media.click_media_act()
# media = driver.find_element_by_xpath("//*[@class = 'siderbar-menu-ul']/li[1]")
# ActionChains(driver).move_to_element(media).perform()
# driver.find_element_by_xpath("html/body/div[1]/section/header/div/div[1]/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/span").click()
sleep(3)
driver.find_element_by_class_name("newActive").click()
sleep(3)
driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[1]/div/div/input").send_keys("123")





sleep(5)
driver.quit()





