import allure
from pages.base_page import BasePage
from all_locators import MainPageLocators, FAQLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Клик по кнопке 'Заказать' в заголовке")
    def click_order_button_header(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

    @allure.step("Клик по кнопке 'Заказать' в футере")
    def click_order_button_footer(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)

    @allure.step("Клик по логотипу 'Самоката'")
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    @allure.step("Клик по логотипу 'Яндекса'")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step('Прокрутка экрана до вопросов.')
    def scroll_to_faq_section(self):
        self.scroll_to_element(FAQLocators.FAQ_SECTION)

    @allure.step('Нажать кнопку "Заказать".')
    def order_button_click(self, location='header'):
        if location == 'header':
            self.click_element(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
            self.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)