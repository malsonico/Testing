from selenium import webdriver
import pytest


@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome(
        executable_path='/Users/marcelo/Desktop/Python/QA/chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.close()
    print("Test Completado")
