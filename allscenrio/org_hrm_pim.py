import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
url='https://opensource-demo.orangehrmlive.com/'

def launch_browser():
    chromeDriver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    chromeDriver.get(url)
    print(chromeDriver.title)
    chromeDriver.maximize_window()
    chromeDriver.save_screenshot('Mainpage.png')
    return chromeDriver

def login_perform():
    loginpage=launch_browser()
    loginpage.find_element_by_id('txtUsername').send_keys('Admin')
    loginpage.find_element_by_id('txtPassword').send_keys('admin123')
    loginpage.find_element_by_id('btnLogin').click()
    return loginpage

def navigate_to_user_page():
    dashbordpage=login_perform()
    mainpim=dashbordpage.find_element_by_id('menu_pim_viewPimModule')
    addemp=dashbordpage.find_element_by_id('menu_pim_addEmployee')
    actions=ActionChains(dashbordpage)
    actions.move_to_element(mainpim).double_click(addemp).perform()

    #add employee
    dashbordpage.find_element_by_id('firstName').send_keys('pandit')
    dashbordpage.find_element_by_id('middleName').send_keys('c')
    dashbordpage.find_element_by_id('lastName').send_keys('patil')

    dashbordpage.find_element_by_id('chkLogin').click()

    dashbordpage.find_element_by_id('user_name').send_keys('pandit')
    dashbordpage.find_element_by_id('user_password').send_keys('Passwordpandit@123')
    dashbordpage.find_element_by_id('re_password').send_keys('Passwordpandit@123')

    dashbordpage.find_element_by_id('btnSave').click()
    return dashbordpage

def close_driver():
    close_element=navigate_to_user_page()
    time.sleep(4)
    close_element.close()
    close_element.quit()

close_driver()