from selenium.common.exceptions import TimeoutException
from Login_Page import LoginPage
from Driver_Page import DriverPage


class TestLogin():

    def test_login(self, driver):
        try:
            login_page = LoginPage(driver)
            driver.get("https://www.saucedemo.com/")

            login_page.enter_username('locked_out_user')
            login_page.enter_password('secret_sauce')
            login_page.click_submit()

        except TimeoutException:
            DriverPage.screenshot("login_error")
