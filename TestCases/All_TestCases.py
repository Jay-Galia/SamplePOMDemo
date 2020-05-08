import unittest
from TestCases.loginTest import LoginTest
from TestCases.directoryTest import DirectorySearchTest
from TestCases.jobTest import SearchTest

tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(DirectorySearchTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(SearchTest)

sanityTestSuite=unittest.TestSuite([tc1,tc2,tc3])

unittest.TextTestRunner().run(sanityTestSuite)