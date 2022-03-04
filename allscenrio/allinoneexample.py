import time
from selenium import webdriver

#chrome setup driver path
CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'

def launch_browser():
    chromeDriver=webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)#create driver object
    chromeDriver.get("https://testautomationpractice.blogspot.com/") #get url
    print("Current Url Name: ",chromeDriver.current_url) #print current url name
    print("Title of Web Page: ",chromeDriver.title) #print web page title
    chromeDriver.maximize_window() #maximize the window
    return chromeDriver

def signup_page():
    chromeBrowser=launch_browser()
    chromeBrowser.find_element_by_id("RESULT_TextField-1").send_keys("Pandit")
    chromeBrowser.find_element_by_id('RESULT_TextField-2').send_keys('Patil')
    chromeBrowser.find_element_by_id('RESULT_TextField-3').send_keys('9623630000')
    chromeBrowser.find_element_by_id('RESULT_TextField-4').send_keys('India')
    chromeBrowser.find_element_by_id('RESULT_TextField-5').send_keys('Pune')
    chromeBrowser.find_element_by_id('RESULT_TextField-6').send_keys('abc@gmail.com')


signup_page()

