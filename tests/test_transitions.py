import pytest
import time
import allure

from page_objects.transitions import Transitions
from data import NAV_BUTTONS


class TestTransitions:

    @allure.title(f'Проверка переходов')
    @pytest.mark.parametrize('button, result', NAV_BUTTONS)
    def test_transitions(self, driver, button, result):

        driver.get('https://qa-scooter.praktikum-services.ru/order')
        transitions = Transitions(driver)
        transitions.click_to_navigation_button(button)
        tabs = driver.window_handles
        time.sleep(2)
        driver.switch_to.window(tabs[-1])
        assert driver.current_url == result
