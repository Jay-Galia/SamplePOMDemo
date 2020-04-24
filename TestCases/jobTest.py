from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest
import HtmlTestRunner
from WebPages.jobPage import AddJob
from WebPages.loginPage import LoginPage
from WebPages.searchUser import SearchUser

class SearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(
        executable_path="D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Drivers/chromedriver.exe")
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    def test_add_job(self):
        driver = self.driver
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
        time.sleep(4)

        search = SearchUser(driver)
        search.click_admin()
        time.sleep(2)

        job = AddJob(driver)
        job.click_job()
        job.click_title()
        job.click_add()
        time.sleep(2)
        job.enter_title("QA Analyst")
        time.sleep(2)
        job.enter_desc("Quality Assurance Engineer responsible for Testing the Software.")
        time.sleep(2)
        job.enter_note("Added on 04/21/2020")
        time.sleep(2)
        job.click_save()
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/PyCharm Workspace/OrangeHRMAutomationDemo/SamplePOMDemo/Reports'))
