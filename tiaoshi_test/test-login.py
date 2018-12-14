#coding:utf-8
from selenium import webdriver
from time import sleep
from case.test_case.test_login_pages import login
from case.test_case.test_add_media_pages import add_media
from selenium.webdriver.common.action_chains import ActionChains
from case.test_case.test_media_add import media_add_jichu
from pages.select_act_pages import Select

#火狐的加载缓存信息
# profile_directory = r"C:\Users\11735\AppData\Roaming\Mozilla\Firefox\Profiles\c3h7won1.default"
# profile = webdriver.FirefoxProfile(profile_directory)
#谷歌加载
# option = webdriver.ChromeOptions()
# option.add_argument('--user-data-dir= C:\\Users\\11735\\AppData\\Local\\Google\\Chrome\\User_Data')

url = "http://testdms.maxuscloud.cn/web/authcenter/index.html#/"
driver = webdriver.Chrome()
login(driver, url)
add_media(driver)
# media_add_jichu(driver)

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

# sleep(3)
# driver.find_element_by_class_name("newActive").click()
# sleep(5)
# #活动名称
# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[1]/div/div/input").send_keys("123")

# #活动目的
# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[2]/div/div/div[1]/input").click()
# driver.find_element_by_xpath("html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()

# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[3]/div/div/div[2]/input").click()
# # #选择车系
# driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[1]").click()
# driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[2]").click()
# driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[3]").click()
# driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[4]").click()
# #时间
# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[1]/div/span/../div/input").send_keys("2018-12-01")
# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[2]/div/span/../div/input").send_keys("2018-12-03")
# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[3]/div/span").click()
# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[3]/div/span/../div/input").send_keys("2018-12-08")
# #一级来源
# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[3]/li[1]/div/span/../div/div/input").click()

# driver.find_element_by_xpath("html/body/div[5]/div[1]/div[1]/ul/li[2]/span").click()
#                                 html/body/div[2]/div[1]/div[1]/ul/li[3]/span

# driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/div/span/../div/textarea").send_keys("jianshu")

# e =driver.find_element_by_class_name("topText").click()



# el-table__body
#这是点击一级来源主动开拓的
# js = "document.querySelectorAll('.el-scrollbar .el-select-dropdown__item')[0].click()"
# driver.execute_script(js)
sleep(5)
# driver.quit()


# document.getElementsByClassName("el-select-dropdown el-popper")[9].style.display= 'block'
