import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from all_locators import OrderFormLocators, RentFormLocators, OrderModalLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Получение заголовка формы оформления заказа.')
    # Получение заголовка формы оформления заказа
    def get_form_title(self):
        # Ищем заголовок относительно кнопки "Далее"
        return self.get_element_text(OrderFormLocators.HEADER_ORDER_NEXT)


    @allure.step('Заполнение поля «Имя» формы данных пользователя.')
    def set_name(self, name):
        self.send_keys(OrderFormLocators.NAME, name)

    @allure.step('Заполнение поля «Фамилия» формы данных пользователя.')
    def set_surname(self, surname):
        self.send_keys(OrderFormLocators.LAST_NAME, surname)

    @allure.step('Заполнение поля «Адрес» формы данных пользователя.')
    def set_address(self, address):
        self.send_keys(OrderFormLocators.ADDRESS, address)

    @allure.step('Заполнение поля «Метро» формы данных пользователя.')
    def set_metro(self, metro):
        self.send_keys(OrderFormLocators.METRO_STATION, metro)
        # Ожидаем появления варианта и кликаем
        self.wait_and_click(OrderFormLocators.METRO_OPTION, timeout=5)

    @allure.step('Заполнение поля «Телефон» формы данных пользователя.')
    def set_phone(self, phone):
        self.send_keys(OrderFormLocators.PHONE, phone)

    @allure.step('Нажатие кнопки «Далее» формы данных пользователя.')
    def next_btn_click(self):
        self.click_element(OrderFormLocators.NEXT_BUTTON)

    @allure.step('Заполнение формы "Для кого самокат".')
    def fill_customer_form(self, name, surname, address, metro, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro(metro)
        self.set_phone(phone)
        self.next_btn_click()

    @allure.step('Заполнение поля «Когда привезти самокат» данных аренды.')
    def set_date(self, date):
        self.send_keys(RentFormLocators.DATE, date)
        self.send_keys(RentFormLocators.DATE, Keys.ENTER)

    @allure.step('Заполнение поля «Срок аренды» формы данных аренды.')
    def set_period(self, period):
        self.click_element(RentFormLocators.RENTAL_PERIOD)
        period_option = (By.XPATH,
                        f"//div[contains(@class, 'Dropdown-option') and contains(text(), '{period}')]")
        self.wait_and_click(period_option, timeout=5)

    @allure.step('Заполнение поля «Цвет самоката» формы данных аренды.')
    def set_color(self, color):
        color_locator = RentFormLocators.COLOR_BLACK if color == 'black' else RentFormLocators.COLOR_GREY
        self.click_element(color_locator)

    @allure.step('Заполнение поля «Комментарий для курьера» данных аренды.')
    def set_comment(self, comment):
        if comment:  # Заполняем только если комментарий не пустой
            self.send_keys(RentFormLocators.COMMENT, comment)

    @allure.step('Нажатие кнопки «Заказать» формы данных аренды.')
    def confirm_btn_click(self):
        self.scroll_to_element(RentFormLocators.ORDER_BUTTON)
        self.click_element(RentFormLocators.ORDER_BUTTON)

    @allure.step('Заполнение формы "Про аренду".')
    def fill_rent_form_and_confirm(self, date, period, color, comment):
        self.set_date(date)
        self.set_period(period)
        self.set_color(color)
        self.set_comment(comment)
        self.confirm_btn_click()

    @allure.step('Получение заголовка окна подтверждения заказа.')
    def get_confirmation_title(self):
        return self.get_element_text(OrderModalLocators.CONFIRM_MODAL)

    @allure.step('Нажатие кнопки «Да» окна подтверждения заказа.')
    def yes_btn_click(self):
        self.click_element(OrderModalLocators.CONFIRM_BUTTON)

    @allure.step('Получение заголовка окна успешного оформления заказа.')
    def get_order_confirmed_title(self):
        return self.get_element_text(OrderModalLocators.SUCCESS_MODAL)

    def create_order(self, customer, rent_options):
        self.fill_customer_form(**customer)
        self.fill_rent_form_and_confirm(**rent_options)
        self.yes_btn_click()