import pytest
from Login_Page import LoginPage


class TestLogin():

    def test_login(self, driver):
        login_page = LoginPage(driver)
        driver.get("https://www.saucedemo.com/")

        login_page.enter_username('standard_user')
        login_page.enter_password('secret_sauce')
        login_page.click_submit()
