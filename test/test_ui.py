import allure
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_ui = config.get("base_url_ui")

@allure.feature("Модуль поиска.")
@allure.title("Тест на поиск фильма или сериала.")
@allure.description("Выполняем поиск фильма или сериала согласно полученным данным.")
@allure.id(1)
@allure.severity("Blocker")
def test_search_film_tv_series(main_page):
    film_tv_series = "Майор Гром: Игра"
    film_name_search_list, film_name_result_search, film_name_personal_page = (
        main_page.search_film_or_tv_series(film_tv_series)
    )
    with allure.step(
        "Проверяем, что переданное название фильма совпадает с названием выводимым в подсказках к модулю поиска, на странице результата поиска, на странице фильма."
    ):
        assert film_tv_series in film_name_search_list[0]
        assert film_name_result_search.startswith(film_tv_series)
        assert film_name_personal_page.startswith(film_tv_series)