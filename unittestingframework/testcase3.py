import unittest

def setupModule():#will be executed before executing any class or any method present in the test class
    print("setupmodule")

def teardownModule():#will be executed after completing everything present in the python module
    print("teardownmodule")

class AppTesting(unittest.TestCase):
    # fixture
    @classmethod
    def setUp(self) -> None:#Execute before all test methods
        print("This is login test")

    @classmethod
    def tearDown(self) -> None: #Execute after all test methods
        print("This is logout test")

    @classmethod
    def setUpClass(cls) -> None: #Execute once when the class is started
        print("Openining application")

    @classmethod
    def tearDownClass(cls) -> None:#Execute once when the class is completed
        print("Close Application")

    def test_search(self):
        print("This is search test")

    def test_advanced_search(self):
        print("This is advanced search test")

    def test_prepaid_recharge(self):
        print("This is prepaid recharge test")

    def test_postpaid_recharge(self):
        print("This is postpaid recharge test")


if __name__ == '__main__':
    unittest.main()
