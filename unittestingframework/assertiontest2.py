import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'
        driver=webdriver.Chrome(CHROME_DRIVER_PATH)
        driver.get("https://www.google.com")
        titleofwebpage=driver.title

        #self.assertTrue(titleofwebpage=="Google") #True
        driver.save_screenshot('Google.png')
        driver.maximize_window()
        self.assertFalse(titleofwebpage=="Google123") #False

        driver.close()


if __name__=='__main__':
    unittest.main()