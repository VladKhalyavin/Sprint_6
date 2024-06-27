import pytest
import allure
from page_objects.order_page import OrderPage
from page_objects.main_page import MainPage
from data import ORDER_FORM_DATA, URL_MAIN_PAGE


class TestOrderPage:
    @allure.title('Создание заказа - успешный заказ')
    @pytest.mark.parametrize('button, station, color', ORDER_FORM_DATA)
    def test_fill_out_the_order_form(self, driver, order_data, button, station, color):
        driver.get(URL_MAIN_PAGE)

        main_page = MainPage(driver)
        main_page.click_to_order_button(button)

        order_page = OrderPage(driver)

        order_page.fill_out_the_order_form(order_data['name'], order_data['surname'], order_data['address'],
                                           station, order_data['phone'], order_data['date'], order_data['period'], color)
        assert driver.find_element(*OrderPage.modal_status_button)
