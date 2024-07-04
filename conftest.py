from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCapcha import Main
from PersonalPage import PersonalPage
from FilmApi import FilmApi
import pytest
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_api = config.get("base_url_api")
token_info = config.get("token_info")

@pytest.fixture
def chrome_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.kinopoisk.ru")
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(chrome_browser):
    return Main(chrome_browser)

@pytest.fixture
def api():
    return FilmApi(base_url_api)


@pytest.fixture()
def film_id(api):
    film_tv_series = "Майор Гром: Игра"
    result_search_by_name, status_code = api.search_film_tv_series_by_name(
        film_tv_series
    )
    assert status_code == 200
    assert result_search_by_name["docs"][0]["name"] == "Майор Гром: Игра"
    print(result_search_by_name["docs"][0]["id"])
    return result_search_by_name["docs"][0]["id"]