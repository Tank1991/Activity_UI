#coding:utf-8
from selenium import webdriver
from time import sleep
from case.test_case.test_login_pages import login
url = "https://test.maxuscloud.cn/web/authcenter/index.html#/"
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












sleep(3)
driver.quit()





