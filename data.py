from page_objects.main_page import MainPage
from page_objects.order_page import OrderPage
from page_objects.transitions import Transitions


#  Адреса тестируемых страниц:
URL_ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
URL_MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
URL_DZEN = 'https://dzen.ru/?yredirect=true'

#  Датасеты для TestMainPage:
#    test_check_accordion_answer:
ANSWER = [(0, 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
          (1, 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать '
              'несколько заказов — один за другим.'),
          (2, 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды '
              'начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная '
              'аренда закончится 9 мая в 20:30.'),
          (3, 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
          (4, 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
          (5, 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без'
              ' передышек и во сне. Зарядка не понадобится.'),
          (6, 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
          (7, 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'), ]

#  Датасеты для TestOrderPage:
#    test_fill_out_the_order_form:
ORDER_FORM_DATA = [(MainPage.nav_order_button, 'Сокольники', OrderPage.checkbox_black),
                   (MainPage.big_order_button, 'Орехово', OrderPage.checkbox_grey)]

NAMES = ['Влад', 'Иван', 'Сергей', 'Антон', 'Никита', 'Глеб', 'Андрей', 'Алексей', 'Владимир']
SURNAMES = ['Смирнов', 'Иванов', 'Скворцов', 'Данилов', 'Шрэков', 'Максимов', 'Коркин', 'Лавров']
STREETS = ['Кудряшова', 'Южная', 'Пушкина', 'Ленина', 'Устюженская', 'Жарова', 'Кавалерийская', 'Садовая']
PERIODS = ['сутки', 'двое суток', 'трое суток', 'четверо суток', 'пятеро суток', 'шестеро суток', 'семеро суток']

#  Датасеты для TestTransitions:
#    test_transitions:
NAV_BUTTONS = [(Transitions.logo_yandex, URL_DZEN, Transitions.search_button),
               (Transitions.logo_scooter, URL_MAIN_PAGE, MainPage.nav_order_button)]
