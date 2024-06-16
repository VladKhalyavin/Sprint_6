import pytest
import allure
from page_objects.main_page import MainPage
from data import ANSWER


class TestMainPage:
    @allure.title(f'Проверка аккордиона с вопросами/ответами')
    @pytest.mark.parametrize('num,result', ANSWER)
    def test_check_accordion_answer(self, driver, num, result):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        main_page = MainPage(driver)
        assert main_page.get_accordion_answer(num) == result

