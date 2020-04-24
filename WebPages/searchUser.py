class SearchUser:

    def __init__(self, driver):
        self.driver = driver

        self.admin_link_id = "menu_admin_viewAdminModule"
        self.management_link_id = "menu_admin_UserManagement"
        self.users_link_id = "menu_admin_viewSystemUsers"
        self.user_textbox_id = "searchSystemUser_userName"
        self.search_button_id = "searchBtn"

    def click_admin(self):
        self.driver.find_element_by_id(self.admin_link_id).click()

    def click_management(self):
        self.driver.find_element_by_id(self.management_link_id).click()

    def click_users(self):
        self.driver.find_element_by_id(self.users_link_id).click()

    def enter_user(self, username):
        self.driver.find_element_by_id(self.user_textbox_id).clear()
        self.driver.find_element_by_id(self.user_textbox_id).send_keys(username)

    def click_search(self):
        self.driver.find_element_by_id(self.search_button_id).click()