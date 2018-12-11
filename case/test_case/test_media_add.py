from selenium import webdriver
from time import sleep

def media_add_jichu(driver):
    #活动目的
    driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[2]/div/div/div[1]/input").click()
    sleep(2)
    driver.find_element_by_xpath("html/body/div[2]/div[1]/div[1]/ul/li[1]/span").click()

    driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[1]/li[3]/div/div/div[2]/input").click()
    # #选择车系
    driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[1]").click()
    driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[2]").click()
    driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[3]").click()
    driver.find_element_by_xpath("html/body/div[3]/div[1]/div[1]/ul/li[4]").click()
    #时间
    driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[1]/div/span/../div/input").send_keys("2018-12-01")
    driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[2]/div/span/../div/input").send_keys("2018-12-03")
    driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[2]/li[3]/div/span/../div/input").send_keys("2018-12-08")
    #一级来源
    driver.find_element_by_xpath("html/body/div[1]/section/section/main/section/div[1]/div[2]/ul[3]/li[1]/div/span/../div/div/input").click()
