from selenium.webdriver.common.by import By


class MainPageLocators:
    """Локаторы главной страницы"""
    ORDER_BUTTON_HEADER = (By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']")
    ORDER_BUTTON_FOOTER = (By.XPATH, "(//button[contains(@class, 'Button_Button') and text()='Заказать'])[2]")

    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")
    YANDEX_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")
    COOKIE_BANNER = (By.ID, "rcc-confirm-button")


class OrderFormLocators:
    """Локаторы формы заказа"""
    NAME = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button")
    PHONE = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    HEADER_ORDER_NEXT = (By.XPATH, "//div[contains(@class, 'Order_Header')]")


class RentFormLocators:
    """Локаторы формы аренды"""
    DATE = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    PERIOD_OPTION = (By.XPATH, "//div[contains(@class, 'Dropdown-option')]")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать' and contains(@class, 'Button_Middle')]")
    PERIOD_OPTION_DROPDOWN = "//div[contains(@class, 'Dropdown-menu')]//div[contains(@class, 'Dropdown-option') and normalize-space()='{}']"




class OrderModalLocators:
    """Локаторы модальных окон"""
    CONFIRM_MODAL = (By.XPATH, "//div[contains(@class, 'Order_Modal')]")
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")
    SUCCESS_MODAL = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")
    STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")

    HEADER_ORDER_FROM = (By.XPATH, "//div[contains(@class, 'Order_Header')]")


class FAQLocators:
    """Локаторы раздела с вопросами"""
    FAQ_SECTION = (By.XPATH, "//div[contains(@class, 'Home_FAQ')]")
    QUESTIONS = (By.XPATH, "//div[@class='accordion__button']")
    ANSWERS = (By.XPATH, "//div[@class='accordion__panel']")
