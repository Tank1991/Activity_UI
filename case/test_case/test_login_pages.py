from pages.login_pages import LoginPage
from time import sleep
def login(driver , url, user = "15250276275" , pwd = "Pass1234"):
    login_page = LoginPage(driver)
    driver.get(url)
    driver.maximize_window()
    try:
        login_page.click_cha()
        login_page.input_user(user)  # 18458333065
        login_page.input_pwd(pwd)
        login_page.input_yzm()
        login_page.click_login_button()
        login_page.click_know()
        #进入活动平台
        login_page.click_huodong()
    except:
        pass













