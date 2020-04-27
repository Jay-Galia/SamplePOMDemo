from select import select

from selenium.webdriver.support.select import Select


class SearchDir:

    def __init__(self, driver):
        self.driver = driver

        self.directory_link_id = "menu_directory_viewDirectory"
        self.name_textbox_id = "searchDirectory_emp_name_empName"
        self.title_dropdown_id = "searchDirectory_job_title"
        self.location_dropdown_id = "searchDirectory_location"
        self.search_button_id = "searchBtn"

    def click_directory(self):
        self.driver.find_element_by_id(self.directory_link_id).click()

    def enter_name(self, name):
        self.driver.find_element_by_id(self.name_textbox_id).clear()
        self.driver.find_element_by_id(self.name_textbox_id).send_keys(name)

    def click_title(self):
        Select(self.driver.find_element_by_id(self.title_dropdown_id)).select_by_visible_text('Sales Executive')

    def click_location(self):
        Select(self.driver.find_element_by_id(self.location_dropdown_id)).select_by_visible_text('    New York Sales Office')

    def click_search(self):
        self.driver.find_element_by_id(self.search_button_id).click()