class AddJob:

    def __init__(self, driver):
        self.driver = driver

        self.job_link_id = "menu_admin_Job"
        self.job_titles_link_id = "menu_admin_viewJobTitleList"
        self.add_button_id = "btnAdd"
        self.title_textbox_id = "jobTitle_jobTitle"
        self.desc_textbox_id = "jobTitle_jobDescription"
        self.note_textbox_id = "jobTitle_note"
        self.save_button_id = "btnSave"

    def click_job(self):
        self.driver.find_element_by_id(self.job_link_id).click()

    def click_title(self):
        self.driver.find_element_by_id(self.job_titles_link_id).click()

    def click_add(self):
        self.driver.find_element_by_id(self.add_button_id).click()

    def enter_title(self, title):
        self.driver.find_element_by_id(self.title_textbox_id).clear()
        self.driver.find_element_by_id(self.title_textbox_id).send_keys(title)

    def enter_desc(self, desc):
        self.driver.find_element_by_id(self.desc_textbox_id).clear()
        self.driver.find_element_by_id(self.desc_textbox_id).send_keys(desc)

    def enter_note(self, note):
        self.driver.find_element_by_id(self.note_textbox_id).clear()
        self.driver.find_element_by_id(self.note_textbox_id).send_keys(note)

    def click_save(self):
        self.driver.find_element_by_id(self.save_button_id).click()