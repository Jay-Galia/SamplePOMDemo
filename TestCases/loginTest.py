from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from WebPages.loginPage import LoginPage
from WebPages.homePage import HomePage

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
        executable_path="D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()

        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Login Successful")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Reports'))