import unittest

class AppTesting(unittest.TestCase):

    @unittest.SkipTest  #skip test
    def test_search(self):
        print("This is search test")

    #skip test with reason
    @unittest.skip("I am skipping this test method because it is not yet ready")
    def test_advancedsearch(self):
        print("This is advanced search method")

    #skip test with condition
    @unittest.skipIf(1==1,"ONE IS EQUALS TO ONE")
    def test_prepaidrecharge(self):
        print("This is prepaid recharge")

    def test_postpaidreacharge(self):
        print("This is postpaid recharge")

    def test_loginbygmail(self):
        print("This is login by email")

    def test_loginbytwitter(self):
        print("This is login by twitter")

if __name__ =='__main__':
    unittest.main