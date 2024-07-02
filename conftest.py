from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from MainPageCapcha import Main
import pytest
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

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