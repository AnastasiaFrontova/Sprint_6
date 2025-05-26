from selenium.webdriver.common.by import By

# Локаторы главной страницы
class MainPageLocators:
    ORDER_BUTTON_HEADER = (By.XPATH, ".//button[text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH, ".//div[contains(@class, 'Home_FinishButton')]//button[text()='Заказать']")

    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Header_LogoYandex')]")
    COOKIE_BANNER = (By.ID, "rcc-confirm-button")

# Локаторы формы заказа
class OrderFormLocators:
    NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")

    METRO_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    METRO_DROPDOWN = (By.CLASS_NAME, "select-search__select")
    METRO_OPTION = (By.XPATH, ".//li[contains(@class, 'select-search__row')]")

    PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")
    HEADER_ORDER_NEXT = (By.XPATH, ".//div[contains(@class, 'Order_Header')]")

# Локаторы формы аренды
class RentFormLocators:
    DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, ".//div[contains(@class, 'Dropdown-root') and .//div[contains(text(), 'Срок аренды')]]")
    PERIOD_OPTION = (
    By.XPATH, ".//div[contains(@class, 'Dropdown-option') and not(contains(@class, 'Dropdown-placeholder'))]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Заказать' and contains(@class, 'Button_Middle')]")

# Локаторы модальных окон
class OrderModalLocators:
    CONFIRM_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_Modal') and contains(text(), 'Хотите оформить заказ')]")
    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, ".//div[contains(@class, 'Order_Modal') and contains(text(), 'Заказ оформлен')]")
    STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']")

# Локаторы раздела с вопросами"
class FAQLocators:
    FAQ_SECTION = (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]")
    QUESTIONS = (By.XPATH, ".//div[contains(@class, 'Home_FAQ')]//div[contains(@class, 'accordion__button')]")
    ANSWERS = (By.XPATH, ".//div[contains(@class, 'accordion__panel') and not(contains(@style, 'hidden'))]")