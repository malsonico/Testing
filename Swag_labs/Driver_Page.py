
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DriverPage:

    def __init__(self, driver):
        self.driver = driver

    def wait_for_element(self, locator):
        espera = WebDriverWait(self.driver, 10)
        elemento = espera.until(EC.visibility_of_element_located(locator))
        return elemento

    def wait_elements(self, locator):
        espera = WebDriverWait(self.driver, 10)
        elemento = espera.until(EC.presence_of_all_elements_located(locator))
        return elemento

    def screenshot(self):
        self.driver_screenshot_as_file
