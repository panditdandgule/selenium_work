from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select

CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

def launch_browser():
    chromeDriver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    chromeDriver.get('https://opensource-demo.orangehrmlive.com/')
    print(chromeDriver.title)
    chromeDriver.maximize_window()
    return chromeDriver

def perform_login():
    chromeDriver=launch_browser()
    chromeDriver.find_element_by_id('txtUsername').send_keys('Admin')
    chromeDriver.find_element_by_id('txtPassword').send_keys('admin123')
    chromeDriver.find_element_by_id('btnLogin').click()
    return chromeDriver

def navigate_to_user():
    dashbord=perform_login()
    recdsh=dashbord.find_element_by_id('menu_recruitment_viewRecruitmentModule')
    revidsh=dashbord.find_element_by_id('menu_recruitment_viewCandidates')

    actions=ActionChains(dashbord)
    actions.move_to_element(recdsh).double_click(revidsh).perform()
    return dashbord

def select_record():
    select=navigate_to_user()
    jobtitle=select.find_element_by_id('candidateSearch_jobTitle')
    Select(jobtitle).select_by_visible_text('Software Engineer')
    vacany=select.find_element_by_id('candidateSearch_jobVacancy')
    Select(vacany).select_by_visible_text('Associate IT Manager')
    hiringmngr=select.find_element_by_id('candidateSearch_hiringManager')
    Select(hiringmngr).select_by_visible_text('Odis Adalwin')
    status=select.find_element_by_id('candidateSearch_status')
    Select(status).select_by_visible_text('Job Offered')
    select.find_element_by_id('candidateSearch_candidateName').send_keys('Pandit')
    select.find_element_by_id('candidateSearch_keywords').send_keys('Project Manager')
    methapp=select.find_element_by_id('candidateSearch_modeOfApplication')
    Select(methapp).select_by_visible_text('Manual')
    select.find_element_by_id('btnSrch').click()

select_record()
