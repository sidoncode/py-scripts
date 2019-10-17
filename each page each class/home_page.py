class Homepage():
    def __init__(self,driver):
        self.driver = driver

        self.welcome_link_id = "welcome"
        self.logout_link_text = "Logout"

    def click_welcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()


    def click_on_logout(self):
        self.driver.find_element_by_id(self.logout_link_text).click()