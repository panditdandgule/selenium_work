import unittest

from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        CHROME_DRIVER_PATH = 'F:\\Scoopons\\selinium_work\\chromedriver_win32\\chromedriver.exe'
        driver=webdriver.Chrome(CHROME_DRIVER_PATH)
        driver.get("https://www.google.com")
        titleofwebpage=driver.title

        #assertEqual()
        #self.assertEqual("Google",titleofwebpage,"Webpage title is not same")
        #self.assertEqual("Google123",titleofwebpage,"Webpage titles are not same")

        #assertNotEqual
        #self.assertNotEqual("Google123",titleofwebpage,"") #both are not not eqal; it will return true
        self.assertNotEqual("Google",titleofwebpage,"Both are Equals")
        driver.save_screenshot('Google.png')
        driver.close()




if __name__=='__main__':
    unittest.main