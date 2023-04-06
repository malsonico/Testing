
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
import os


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

    def screenshot(self, name):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        screenshot_name = f"{name}_{timestamp}.png"
        screenshots_directory = '/Users/marcelo/Desktop/Python/QA/Swag_Labs/Error_screenshots/'
        screenshot_path = os.path.join(screenshots_directory, screenshot_name)
        self.driver.get_screenshot_as_file(screenshot_path)
        return screenshot_path
