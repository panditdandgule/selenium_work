import  unittest


class Test(unittest.TestCase):
    def test_name(self):
        list=["python","selenium","java"]

        self.assertIn("python",list)
        self.assertIn("c++",list)
        self.assertNotIn("ruby",list)

if __name__=='__main__':
    unittest.main()