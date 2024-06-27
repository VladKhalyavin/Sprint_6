# Форма "Для кого самокат":

NAME_INPUT = '//input[@placeholder="* Имя"]'
SURNAME_INPUT = '//input[@placeholder="* Фамилия"]'
ADDRESS_INPUT = '//input[@placeholder="* Адрес: куда привезти заказ"]'
STATION_INPUT = '//input[@placeholder="* Станция метро"]'
STATION_SELECT_BUTTON = '//div[@class="select-search__select"]/ul/li[@data-index="0"]/button'
PHONE_INPUT = '//input[@placeholder="* Телефон: на него позвонит курьер"]'

# Форма "Про аренду":

DATE_INPUT = '//input[@placeholder="* Когда привезти самокат"]'
PERIOD_INPUT = '//span[@class="Dropdown-arrow"]'
PERIOD_OPTIONS = '//div[@class="Dropdown-menu"]/div[text()="{}"]'
CHECKBOX_BLACK = '//label[@for="black"]'
CHECKBOX_GREY = '//label[@for="grey"]'
COMMENT_INPUT = '//input[@placeholder="Комментарий для курьера"]'


CONFIRM_BUTTON = '//button[contains(@class, "Button_Middle") and (text()="Далее")]'  # Кнопка "Даллее" в форме
FORM_ORDER_BUTTON = '//button[contains(@class, "Button_Middle") and (text()="Заказать")]'  # Кнопка "Заказать" в форме
YES_ORDER_BUTTON = '//button[contains(@class, "Button_Middle") and (text()="Да")]'  # Кнопка "Да" в модальном окне
MODAL_STATUS_BUTTON = ('//div[contains(@class, "Order_Modal")]//button[contains(@class, "Button_Middle") '
                       'and (text()="Посмотреть статус")]')  # кнопка "Посмотреть статус в модальном окне"
