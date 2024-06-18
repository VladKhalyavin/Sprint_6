import pytest
from selenium import webdriver
from halper import RandomOrderData


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def order_data():
    order_data = {'name': RandomOrderData.random_name(),
                  'surname': RandomOrderData.random_surname(),
                  'address': RandomOrderData.random_address(),
                  'phone': RandomOrderData.random_phone_number(),
                  'date': RandomOrderData.order_date(),
                  'period': RandomOrderData.random_period()}
    return order_data
