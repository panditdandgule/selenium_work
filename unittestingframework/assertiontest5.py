import unittest

class Test(unittest.TestCase):
    def test_name(self):
        #self.assertGreater(100,10) #first number should be greater

        #self.assertGreater(100,10) #first number greater or equal

        #self.assertLess(10,100) #first number should be less then testcase pass

        self.assertLessEqual(10,100)

if __name__=='__main__':
    unittest.main()