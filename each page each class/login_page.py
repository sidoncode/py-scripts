from selenium import webdriver

class loginpage():
    def __init__(self,driver):
        self.driver = driver

        self.username_testbox_id = "txtUsername"
        self.password.testbox_id = "txtPassword"
        self.login_button_id = "btnLogin"

    def enter_username(self,username):
        self.driver.find_element_by_id(self.username_testbox_id).clear()
        self.driver.find_element_by_id(self.username_testbox_id).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element_by_id(self.password.testbox_id).clear()
        self.driver.find_element_by_id(self.password.testbox_id).send_keys(password)
    def click_login_btn(self):
        self.driver.find_element_by_id(self.login_button_id).click()
