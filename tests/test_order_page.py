import allure
import pytest

from data import TEST_SCENARIOS, PAGE_SECTION_TITLES
from all_locators import MainPageLocators
from pages.order_page import OrderPage
from pages.main_page import MainPage


class TestOrderPage:
    @allure.title('Создание заказа через разные точки входа')
    @pytest.mark.parametrize(
        'scenario',
        [
            pytest.param(TEST_SCENARIOS[0], id='Кнопка в хедере'),
            pytest.param(TEST_SCENARIOS[1], id='Кнопка в футере')
        ],
        scope="function"
    )
    def test_create_order_from_different_entry_points(self, driver, scenario):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        if scenario['entry_point'] == 'header':
            main_page.click_element(MainPageLocators.ORDER_BUTTON_HEADER)
        else:
            main_page.scroll_to_element(MainPageLocators.ORDER_BUTTON_FOOTER)
            main_page.click_element(MainPageLocators.ORDER_BUTTON_FOOTER)

        order_page = OrderPage(driver)
        order_page.create_order(scenario['customer'], scenario['rent'])

        success_title = order_page.get_order_confirmed_title()
        assert PAGE_SECTION_TITLES['success'] in success_title, (
            f'Ожидался заголовок "{PAGE_SECTION_TITLES["success"]}", '
            f'но получен "{success_title}"'
        )

    @allure.title('Проверка перехода на страницу заказа')
    def test_order_page_opens_correctly(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

        order_page = OrderPage(driver)
        assert "Про аренду" not in order_page.driver.page_source  # Проверяем что мы на первой странице