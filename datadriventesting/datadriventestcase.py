import xelutil
from selenium import webdriver
import time

CHROMEDRIVERPATH=r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

chromeDriver=webdriver.Chrome(executable_path=CHROMEDRIVERPATH)
chromeDriver.get('https://opensource-demo.orangehrmlive.com/')

chromeDriver.maximize_window()

path='F:\Scoopons\selinium_work\selenium_codes\datadriventesting\logindata.xlsx'

rowsCount=xelutil.getRowCount(path,"Sheet1")


for row in range(2,rowsCount+1):
    username=xelutil.readData(path,"Sheet1",row,1)
    password=xelutil.readData(path,"Sheet1",row,2)

    chromeDriver.find_element_by_id('txtUsername').send_keys(username)
    chromeDriver.find_element_by_id('txtPassword').send_keys(password)
    chromeDriver.find_element_by_id('btnLogin').click()


    if chromeDriver.title=="Welcome Paul":
        print("Test case passed")
        xelutil.writeData(path,"Sheet1",row,3,"test passed")
        time.sleep(2)
        chromeDriver.close()
    else:
        print("test failed")
        xelutil.writeData(path,"Sheet1",row,3,"test failed")
        time.sleep(2)
        chromeDriver.close()

    chromeDriver.get('https://opensource-demo.orangehrmlive.com/')



time.sleep(5)
chromeDriver.quit()