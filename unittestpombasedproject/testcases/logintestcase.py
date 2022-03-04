import time
import unittest
from selenium import webdriver
import HtmlTestRunner

#It will add this path in our enviornment variable and it will help to run this project through cmd prompt
import sys
sys.path.append('F:\\Scoopons\\selinium_work\\selenium_codes\\unittestpombasedproject')
from selenium_codes.unittestpombasedproject.pageobjects.loginpage import LoginPage


class LoginTest(unittest.TestCase):
    baseURL="http://admin-demo.nopcommerce.com/"
    userName="admin@yourstore.com"
    password="admin"
    CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    reportsPath=r'F:\Scoopons\selinium_work\selenium_codes\unittestpombasedproject\reports'

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver.get(cls.baseURL)
        cls.driver.maximize_window()
        
    def test_login(self):
        lp=LoginPage(self.driver)
        lp.setUserName(self.userName)
        lp.setPassword(self.password)
        lp.clickLogin()
        time.sleep(5)
        lp.clickLogout()
        
        self.assertEqual("Dashboard / nopCommerce administration",self.driver.title,"Webpage title is not matched.")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        
if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=LoginTest.reportsPath))