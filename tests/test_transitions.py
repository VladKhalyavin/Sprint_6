import pytest
import allure

from page_objects.transitions import Transitions
from data import NAV_BUTTONS, URL_ORDER_PAGE


class TestTransitions:

    @allure.title(f'Проверка переходов')
    @pytest.mark.parametrize('button, result, target', NAV_BUTTONS)
    def test_transitions(self, driver, button, result, target):

        driver.get(URL_ORDER_PAGE)
        transitions = Transitions(driver)
        transitions.click_to_navigation_button(button)
        tabs = driver.window_handles
        driver.switch_to.window(tabs[-1])
        transitions.find_element_with_wait(target)
        assert driver.current_url == result
