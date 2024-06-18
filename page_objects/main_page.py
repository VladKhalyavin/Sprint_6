import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from locators.main_page_locators import QUESTION_LOCATOR, ANSWER_LOCATOR, BIG_ORDER_BUTTON, NAV_ORDER_BUTTON


class MainPage(BasePage):

    question = [By.XPATH, QUESTION_LOCATOR]
    answer = [By.XPATH, ANSWER_LOCATOR]
    big_order_button = [By.XPATH, BIG_ORDER_BUTTON]
    nav_order_button = [By.XPATH, NAV_ORDER_BUTTON]

    @allure.step('Нажать кнопку "Заказать"')
    def click_to_order_button(self, button_locator):
        self.scroll_to_element(button_locator)
        self.click_to_element(button_locator)

    @allure.step('Прокрутка страницы до аккордиона')
    def scroll_to_accordion(self):
        locator_last_question = self.format_locators(self.question, 7)
        self.scroll_to_element(locator_last_question)

    @allure.step('Раскрытие аккордиона')
    def click_to_accordion(self, num):
        locator_question = self.format_locators(self.question, num)
        self.find_element_with_wait(locator_question)
        self.click_to_element(locator_question)

    @allure.step('Получение текста ответа')
    def get_text_answer(self, num):
        locator_answer = self.format_locators(self.answer, num)
        return self.get_text_from_element(locator_answer)

    def get_accordion_answer(self, num):
        self.scroll_to_accordion()
        self.click_to_accordion(num)
        return self.get_text_answer(num)
