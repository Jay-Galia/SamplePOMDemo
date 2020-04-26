from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from WebPages.loginPage import LoginPage
from WebPages.directoryPage import SearchDir

class DirectorySearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
        executable_path="D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_directory(self):
        driver = self.driver
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(3)

        directory = SearchDir(driver)
        directory.click_directory()
        time.sleep(2)
        directory.enter_name("Russel Hamilton")
        time.sleep(2)
        directory.click_title()
        time.sleep(2)
        directory.click_search()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
            cls.driver.close()
            cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Reports'))
