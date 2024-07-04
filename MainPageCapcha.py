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
                By.CSS_SELECTOR, "CheckboxCaptcha-Button"
            ).click()
        except NoSuchElementException:
            pass

    @allure.step(
        "Переходим на сайт Кинопоиск. Выполняем поиск фильма или сериала. Название - {info_to_search}."
    )
    def search_film_or_tv_series(self, info_to_search: str) -> str:
        """Метод позволяет выполнить поиск фильма или сериала
        используя информацию полученную на вход.
        Открыть персональную карточку фильма или сериала.
        Args:
            info_to_search (str): название фильма или сериала.
        Returns:
            str: возвращает название фильма или сериала из подсказки к поисковому полю, страницы результата поиска, персональной страницы фильма или сериала.
        """
        self.captcha()
        self.enter_search_info(info_to_search)
        found_movie_titles = self.get_search_field_list("[id^='suggest-item']")
        self.click_search_button()
        a_film_link, film_text_link = self.get_element_from_search_result_page(
            "div.element.most_wanted"
        )
        a_film_link.click()

        with allure.step("На странице фильма или сериала получаем его название."):
            name_film_personal_page = WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, "h1[itemprop='name']")
                )
            )

        with allure.step(
            "Возвращаем список с 1 фильмом или сериалом из подсказки к поисковому полю, название фильма или сериала на странице результата поиска"
        ):
            return (
                found_movie_titles,
                film_text_link,
                name_film_personal_page.text,
            )

    @allure.step("Вводим данные в поле поиска: {info_to_search}")
    def enter_search_info(self, info_to_search: str):
        """
        Данный метод вводит данные в поисковое поле.
        Args:
            info_to_search (str): информация для поиска.
        """
        search_field = self._driver.find_element(
            By.CSS_SELECTOR,
            "input[kinopoisk-header-search-form-input__input]",
        )
        search_field.click()
        search_field.send_keys(info_to_search)

