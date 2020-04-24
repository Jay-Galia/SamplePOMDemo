class AddCandidate:

    def __init__(self, driver):
        self.driver = driver

        self.recruitment_link_id = "menu_recruitment_viewRecruitmentModule"
        self.candidate_link_id = "menu_recruitment_viewCandidates"
        self.add_button_id = "btnAdd"
        self.first_textbox_id = "addCandidate_firstName"
        self.last_textbox_id = "addCandidate_lastName"
        self.email_textbox_id = "addCandidate_email"
        self.comment_textbox_id = "addCandidate_comment"
        self.consent_checkbox_id = "addCandidate_consentToKeepData"
        self.save_button_id = "btnSave"

    def click_recruitment(self):
        self.driver.find_element_by_id(self.recruitment_link_id).click()

    def click_candidate(self):
        self.driver.find_element_by_id(self.candidate_link_id).click()

    def click_add(self):
        self.driver.find_element_by_id(self.add_button_id).click()

    def enter_first(self, first):
        self.driver.find_element_by_id(self.first_textbox_id).clear()
        self.driver.find_element_by_id(self.first_textbox_id).send_keys(first)

    def enter_last(self, last):
        self.driver.find_element_by_id(self.last_textbox_id).clear()
        self.driver.find_element_by_id(self.last_textbox_id).send_keys(last)

    def enter_email(self, email):
        self.driver.find_element_by_id(self.email_textbox_id).clear()
        self.driver.find_element_by_id(self.email_textbox_id).send_keys(email)

    def enter_comment(self, comment):
        self.driver.find_element_by_id(self.comment_textbox_id).clear()
        self.driver.find_element_by_id(self.comment_textbox_id).send_keys(comment)

    def click_consent(self):
        self.driver.find_element_by_id(self.consent_checkbox_id).click()

    def click_save(self):
        self.driver.find_element_by_id(self.save_button_id).click()