from selenium.webdriver.common.by import By
from Driver_Page import DriverPage


class CartPage(DriverPage):

    def __init__(self, driver):
        self.driver = driver

        self.btn_continue_shopping_id = (By.ID, 'continue-shopping')
        self.btn_checkout_id = (By.ID, 'checkout')
        self.btn_remove_item = (
            By.XPATH, "//button[contains(text(), 'Remove')]")

    def remove_item(self):
        self.wait_for_element(self.btn_remove_item).click()

    def continue_shopping(self):
        self.wait_for_element(self.btn_continue_shopping_id).click()

    def checkout(self):
        self.wait_for_element(self.btn_checkout_id).click()
