from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from WebPages.loginPage import LoginPage
from WebPages.addCandidate import AddCandidate

class AddCandidateTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
        executable_path="D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_candidate(self):
        driver = self.driver
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(3)

        candidate = AddCandidate(driver)
        candidate.click_recruitment()
        candidate.click_candidate()
        time.sleep(3)
        candidate.click_add()
        candidate.enter_first("John")
        time.sleep(1)
        candidate.enter_last("Cena")
        time.sleep(1)
        candidate.enter_email("johncena@gmail.com")
        time.sleep(1)
        candidate.enter_comment("This is a test user")
        candidate.click_consent()
        time.sleep(1)
        candidate.click_save()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Reports'))