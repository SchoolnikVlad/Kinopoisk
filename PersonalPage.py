from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class PersonalPage:

    def __init__(self, driver: WebDriver):
        self._driver = driver

    def find_element_and_click(self, css_selector: str):
        """
        Данный метод находит элемент на странице по его
        селектору и нажимает на элемент.
        Args:
            css_selector (str): css_selector элемента.
        """
        element = WebDriverWait(self._driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector))
        )
        element.click()

    def find_element_and_return_text(
        self, element: WebElement, css_selector: str
    ) -> str:
        """
        Данный метод находит элемент на странице по его селектору
        и возращает текст данного элемента.
        Args:
            element: WebElement.
            css_selector (str): css_selector элемента.
        Returns:
            str: текст элемента.
        """
        element = WebDriverWait(element, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, css_selector))
        )
        return element.text

    def find_button_change_delete_by_text(self, button_text: str) -> WebElement:
        """
        Метод для поиска кнопки по тексту. Две подкнопки 'Изменить оценку' и 'Удалить оценку'.
        Args:
            button_text (str): текст кнопки для поиска.
        Returns:
            WebElement: найденная кнопка.
        """
        buttons = WebDriverWait(self._driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "button[class^='style_root']")
            )
        )
        for button in buttons:
            if button.text == button_text:
                return button