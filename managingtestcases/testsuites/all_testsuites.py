import unittest

from managingtestcases.package1.tc_logintest import LoginTest
from managingtestcases.package1.tc_signuptest import SignupTest

from managingtestcases.package2.tc_paymentreturns import PaymentReturnsTest
from managingtestcases.package2.tc_paymenttest import PaymentTest

# Get all tests from LoginTest,SignupTest,PaymentTest and PaymentReturnsTest\
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)

# Creating test suites
sanityTestSuite = unittest.TestSuite([tc1, tc2])  # Sanity test suite
functionalTestSuite = unittest.TestSuite([tc3, tc4])  # functional test suite
masterTestSuite = unittest.TestSuite([tc1, tc2, tc3, tc4])  # master test suite

# unittest.TextTestRunner().run(sanityTestSuite)
# unittest.TextTestRunner().run(functionalTestSuite)
unittest.TextTestRunner(verbosity=2).run(masterTestSuite)
