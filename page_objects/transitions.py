import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from locators.transitions_locators import LOGO_YANDEX, LOGO_SCOOTER


class Transitions(BasePage):
    logo_yandex = [By.XPATH, LOGO_YANDEX]
    logo_scooter = [By.XPATH, LOGO_SCOOTER]

    @allure.step('Переход на страницу по нажатию кнопки навигационной панели')
    def click_to_navigation_button(self, logo):
        self.click_to_element(logo)
