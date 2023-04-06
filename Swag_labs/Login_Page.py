from selenium.webdriver.common.by import By
from Driver_Page import DriverPage


class LoginPage(DriverPage):

    def __init__(self, driver):
        self.driver = driver

        self.username_input_id = (By.ID, "user-name")
        self.password_input_id = (By. ID, "password")
        self.submit_button_id = (By. ID, "login-button")

    def enter_username(self, username):
        self.wait_for_element(self.username_input_id).send_keys(username)

    def enter_password(self, password):
        self.wait_for_element(self.password_input_id).send_keys(password)

    def click_submit(self):
        self.wait_for_element(self.submit_button_id).click()
