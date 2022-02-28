import unittest

from selenium import webdriver

class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        print('Step1 - Launch Browser Instance')
        CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://www.google.com")
        print("Title of the page is: ",self.driver.title)
        self.driver.close()


    def test_bing(self):
        print('Step1 - Launch Browser Instance')
        CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.driver.get("https://www.bing.com")
        print("Title of the page is: ",self.driver.title)
        self.driver.close()

if __name__=='__main__':
    unittest.main()