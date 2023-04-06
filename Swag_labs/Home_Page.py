from selenium.webdriver.common.by import By
from Driver_Page import DriverPage
import random
import time


class HomePage(DriverPage):

    def __init__(self, driver):
        self.driver = driver

        self.menu_burger_id = (By.ID, 'react-burger-menu-btn')
        self.logout_id = (By.ID, 'logout_sidebar_link')
        self.allitems_id = (By.ID, 'inventory_sidebar_link')
        self.products_xpath = (By.XPATH, "//div[@class='inventory_item_name']")
        self.sort_xpath = (By.XPATH, "//span[@class='active_option']")
        self.cart_id = (By.ID, 'shopping_cart_container')
        self.add_to_cart_xpath = (
            By.XPATH, "//button[contains(text(), 'Add to cart')]")

    def select_item_to_buy(self):
        select_item = self.wait_elements(self.products_xpath)
        seleccion = random.choice(select_item)
        seleccion.click()

    def add_to_cart(self):
        self.wait_for_element(self.add_to_cart_xpath).click()

    def check_cart(self):
        self.wait_for_element(self.cart_id).click()
        time.sleep(3)

    def menu_burger(self):
        self.wait_for_element(self.menu_burger_id).click()

    def logout(self):
        self.wait_for_element(self.logout_id).click()
