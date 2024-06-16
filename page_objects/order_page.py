import allure
from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from locators.order_page_locators import (NAME_INPUT, SURNAME_INPUT, ADDRESS_INPUT, STATION_INPUT,
                                          STATION_SELECT_BUTTON, PHONE_INPUT, PERIOD_OPTIONS,
                                          DATE_INPUT, PERIOD_INPUT, CHECKBOX_GREY, CHECKBOX_BLACK, CONFIRM_BUTTON,
                                          FORM_ORDER_BUTTON, YES_ORDER_BUTTON, MODAL_STATUS_BUTTON)


class OrderPage(BasePage):
    name_input = [By.XPATH, NAME_INPUT]
    surname_input = [By.XPATH, SURNAME_INPUT]
    address_input = [By.XPATH, ADDRESS_INPUT]
    station_input = [By.XPATH, STATION_INPUT]
    station_select = [By.XPATH, STATION_SELECT_BUTTON]
    phone_input = [By.XPATH, PHONE_INPUT]
    date_input = [By.XPATH, DATE_INPUT]
    period_input = [By.XPATH, PERIOD_INPUT]
    period_options = [By.XPATH, PERIOD_OPTIONS]
    confirm_button = [By.XPATH, CONFIRM_BUTTON]
    form_order_button = [By.XPATH, FORM_ORDER_BUTTON]
    yes_order_button = [By.XPATH, YES_ORDER_BUTTON]
    checkbox_black = [By.XPATH, CHECKBOX_BLACK]
    checkbox_grey = [By.XPATH, CHECKBOX_GREY]
    modal_status_button = [By.XPATH, MODAL_STATUS_BUTTON]

    @allure.step('Заполнить поле "Имя"')
    def set_name(self, name):
        self.add_text_to_element(self.name_input, name)

    @allure.step('Заполнить поле "Фамилия"')
    def set_surname(self, surname):
        self.add_text_to_element(self.surname_input, surname)

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.add_text_to_element(self.address_input, address)

    @allure.step('Заполнить поле "Станция метро"')
    def set_station(self, station):
        self.add_text_to_element(self.station_input, station)
        self.click_to_element(self.station_select)

    @allure.step('Заполнить поле "Номер телефона"')
    def set_phone(self, phone):
        self.add_text_to_element(self.phone_input, phone)

    @allure.step('Нажать "Далее"')
    def click_to_confirm(self):
        self.click_to_element(self.confirm_button)

    @allure.step('Нажать "Заказать"')
    def click_to_order(self):
        self.click_to_element(self.form_order_button)

    @allure.step('Нажать "Да" в модальном окне')
    def click_to_yes_order_button(self):
        self.click_to_element(self.yes_order_button)

    @allure.step('Заполнить поле "Когда привезти самокат"')
    def set_date(self, date):
        self.add_text_to_element(self.date_input, date)

    @allure.step('Выбрать срок аренды')
    def set_period(self, period):
        self.click_to_element(self.period_input)
        period = self.format_locators(self.period_options, period)
        self.scroll_to_element(period)
        self.click_to_element(period)

    @allure.step('Выбрыть цвет самоката')
    def set_scooter_color(self, color):
        self.click_to_element(color)

    def fill_out_the_order_form(self, name, surname, address, station, phone, date, period, color):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_station(station)
        self.set_phone(phone)
        self.click_to_confirm()
        self.set_date(date)
        self.set_period(period)
        self.set_scooter_color(color)
        self.click_to_order()
        self.click_to_yes_order_button()


