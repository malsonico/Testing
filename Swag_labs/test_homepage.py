
import pytest

from Home_Page import HomePage
from Login_Page import LoginPage
from Cart_Page import CartPage
from selenium.common.exceptions import TimeoutException


class TestHome():

    def test_buy_item(self, driver):
        login_page = LoginPage(driver)
        home_page = HomePage(driver)
        cart_page = CartPage(driver)

        try:
            driver.get("https://www.saucedemo.com/")

            login_page.enter_username('standard_user')
            login_page.enter_password('secret_sauce')
            login_page.click_submit()

        except TimeoutException:
            pytest.fail("La pagina no se cargo correctamente")

        else:
            try:
                home_page.select_item_to_buy()
                home_page.add_to_cart()
                home_page.check_cart()

            except TimeoutException:
                pytest.fail("La pagina no se cargo correctamente")

            else:
                try:
                    cart_page.remove_item()
                    cart_page.continue_shopping()
                except TimeoutException:
                    pytest.fail("La pagina no se cargo correctamente")

        finally:
            home_page.menu_burger()
            home_page.logout()
