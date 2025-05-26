from data import TEST_SCENARIOS, PAGE_SECTION_TITLES
import allure
import pytest
from all_locators import MainPageLocators, OrderFormLocators
from pages.order_page import OrderPage
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL, ORDER_PAGE_URL, DZEN_REDIRECT_URL


class TestOrderPage:
    @allure.title('Создание заказа через разные точки входа')
    @pytest.mark.parametrize(
        'entry_point_locator, scenario_index',
        [
            pytest.param(MainPageLocators.ORDER_BUTTON_HEADER, 0, id='Кнопка в хедере'),
            pytest.param(MainPageLocators.ORDER_BUTTON_FOOTER, 1, id='Кнопка в футере')
        ]
    )
    def test_create_order_from_different_entry_points(self, driver, entry_point_locator, scenario_index):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()

        # Добавила скролл к элементу
        main_page.scroll_to_element(entry_point_locator)
        main_page.wait_and_click(entry_point_locator)

        order_page = OrderPage(driver)
        scenario = TEST_SCENARIOS[scenario_index]
        order_page.create_order(scenario['customer'], scenario['rent'])

        success_title = order_page.get_order_confirmed_title()
        assert PAGE_SECTION_TITLES['success'] in success_title, (
            f'Ожидался заголовок "{PAGE_SECTION_TITLES["success"]}", '
            f'но получен "{success_title}"'
        )

    @allure.title('Проверка корректного открытия страницы заказа')
    def test_order_page_opens_correctly(self, driver):
        main_page = MainPage(driver)
        main_page.open()
        main_page.accept_cookies()
        main_page.click_element(MainPageLocators.ORDER_BUTTON_HEADER)

        order_page = OrderPage(driver)

        # Проверяем URL страницы заказа
        order_page.wait_for_url_contains(ORDER_PAGE_URL)

        # Проверяем видимость формы для ввода данных клиента
        order_page.wait_for_visibility(OrderFormLocators.NAME)

        # Проверяем наличие всех обязательных полей
        required_fields = [
            (OrderFormLocators.NAME, "Поле 'Имя'"),
            (OrderFormLocators.LAST_NAME, "Поле 'Фамилия'"),
            (OrderFormLocators.ADDRESS, "Поле 'Адрес'"),
            (OrderFormLocators.METRO_STATION, "Поле 'Станция метро'"),
            (OrderFormLocators.PHONE, "Поле 'Телефон'"),
            (OrderFormLocators.NEXT_BUTTON, "Кнопка 'Далее'")
        ]

        for locator, field_name in required_fields:
            assert order_page.is_element_displayed(locator), f"{field_name} не отображается"
