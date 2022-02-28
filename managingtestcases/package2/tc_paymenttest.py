import unittest

class PaymentTest(unittest.TestCase):
    def test_paymentindoller(self):
        print("This is payment in doller test")
        self.assertTrue(True)

    def test_paymentinrupees(self):
        print("This is payment in rupees test")
        self.assertTrue(True)

if __name__=='__main__':
    unittest.main()