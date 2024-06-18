import pytest
import allure
from halper import RandomOrderData
from page_objects.order_page import OrderPage
from page_objects.main_page import MainPage
from data import ORDER_FORM_DATA, URL_MAIN_PAGE


class TestOrderPage:
    @allure.title('Создание заказа - успешный заказ')
    @pytest.mark.parametrize('button, station, color', ORDER_FORM_DATA)
    def test_fill_out_the_order_form(self, driver, button, station, color):
        driver.get(URL_MAIN_PAGE)

        main_page = MainPage(driver)
        main_page.click_to_order_button(button)

        order_page = OrderPage(driver)

        name = RandomOrderData.random_name()
        surname = RandomOrderData.random_surname()
        address = RandomOrderData.random_address()
        phone = RandomOrderData.random_phone_number()
        date = RandomOrderData.order_date()
        period = RandomOrderData.random_period()

        order_page.fill_out_the_order_form(name, surname, address, station, phone, date, period, color)
        assert driver.find_element(*OrderPage.modal_status_button)
