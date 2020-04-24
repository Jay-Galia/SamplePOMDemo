from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from SamplePOMDemo.WebPages.searchUser import SearchUser
from SamplePOMDemo.WebPages.loginPage import LoginPage


class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
        executable_path="D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()
        # cls.driver.get("https://opensource-demo.orangehrmlive.com/")
        # cls.driver.enter_username("Admin")
        # cls.driver.enter_password("admin123")
        # cls.driver.click_login()

    def test_search(self):
        # LoginTest.test_login_valid(self)
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(3)
        # driver = self.driver
        search = SearchUser(driver)
        search.click_admin()
        search.click_management()
        search.click_users()
        search.enter_user("Hannah Flores")
        search.click_search()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Reports'))
