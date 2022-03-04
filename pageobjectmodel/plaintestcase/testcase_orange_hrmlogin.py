import unittest
from selenium import webdriver
import HtmlTestRunner

url = 'https://opensource-demo.orangehrmlive.com/'
reportspath=r'F:\Scoopons\selinium_work\selenium_codes\pageobjectmodel\plaintestcase\reports'

class OrangeHRMTest(unittest.TestCase):

    # this is fixture method
    @classmethod
    def setUpClass(cls) -> None:
        CHROME_DRIVER_PATH = r'F:\Scoopons\selinium_work\chromedriver_win32\chromedriver.exe'

        cls.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        cls.driver.maximize_window()

    def test_homepagetitle_verification(self):
        self.driver.get(url)
        self.assertEqual("OrangeHRM", self.driver.title,
                         "Web page title is not matched")  # if title not matched then message will print

    def test_login(self):
        self.driver.get(url)
        self.driver.find_element_by_id('txtUsername').send_keys('Admin')
        self.driver.find_element_by_id('txtPassword').send_keys('admin123')
        self.driver.find_element_by_id('btnLogin').click()
        self.assertEqual("OrangeHRM", self.driver.title, "Web page title is not matched")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
        print("Test completed..")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=reportspath))