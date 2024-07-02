from typing import Tuple, List
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import allure

class Main:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @allure.step("Обрабатываем капчу, если она появляется.")
    def captcha(self):
        """
        Данный метод обрабатывает капчу.
        """
        try:
            self._driver.find_element(
                By.CSS_SELECTOR, ".CheckboxCaptcha-Button"
            ).click()
        except NoSuchElementException:
            pass