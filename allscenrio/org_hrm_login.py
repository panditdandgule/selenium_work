from selenium import webdriver

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
#generic Script --? pass on url -- it will simply website landing page open kar k dega..
def login_page(app_url):

    chromeDriver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    chromeDriver.get(app_url)
    chromeDriver.maximize_window()
    return chromeDriver

def perform_login():
    chromeDriver = login_page('https://opensource-demo.orangehrmlive.com/')
    chromeDriver.find_element_by_id('txtUsername').send_keys('Admin')
    chromeDriver.find_element_by_id('txtPassword').send_keys('admin123')
    chromeDriver.find_element_by_id('btnLogin').click()
    return chromeDriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select #singlechoice/multichoice

def navigate_to_users_page():
    dashboardPage = perform_login()
    ActionChains(dashboardPage).move_to_element(dashboardPage.find_element_by_id('menu_admin_viewAdminModule'))\
        .move_to_element(dashboardPage.find_element_by_id('menu_admin_UserManagement')).move_to_element(dashboardPage.find_element_by_id('menu_admin_viewSystemUsers')).click()\
        .perform()
    return dashboardPage

def check_role_selection(role):
    usersPage = navigate_to_users_page()
    userRoleDrpDwn =Select(usersPage.find_element_by_id('searchSystemUser_userType'))
    userRoleDrpDwn.select_by_visible_text(role)
    usersPage.find_element_by_id('searchBtn').click()
    return usersPage

def select_records(role):
    specificRoles = check_role_selection(role)
    resultTable = specificRoles.find_element_by_id('resultTable')
    table_body = resultTable.find_element_by_tag_name('tbody')
    rows = table_body.find_elements_by_tag_name('tr')
    for row in rows:
        columns = row.find_elements_by_tag_name('td')
        if columns[2].text == 'ESS':
            columns[0].find_element_by_tag_name('input').click()



select_records('All')

#menu_admin_UserManagement
#TOOLSQA
#launch_browser('https://demoqa.com/automation-practice-form/')
#ORGANGHRM

#navigate_to_users_page()
import time
time.sleep(30)