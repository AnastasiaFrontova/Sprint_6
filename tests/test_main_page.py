import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from urls import MAIN_PAGE_URL, ORDER_PAGE_URL, DZEN_REDIRECT_URL



@allure.feature("Main Page")
class TestMainPageRedirects:
    """Тесты редиректов с главной страницы."""

    @allure.story("Redirect to main page after clicking on the scooter logo")
    def test_scooter_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Принятие куки"):
            main_page.accept_cookies()

        with allure.step("Клик по логотипу 'Самоката'"):
            main_page.click_scooter_logo()

        with allure.step("Проверка редиректа на главную страницу"):
            main_page.wait_for_url_contains(MAIN_PAGE_URL)
            assert MAIN_PAGE_URL in driver.current_url, \
                f"Expected URL containing {MAIN_PAGE_URL}, got {driver.current_url}"


    @allure.story("Redirect to Dzen after clicking on the Yandex logo")
    def test_yandex_logo_redirect(self, driver):
        main_page = MainPage(driver)

        with allure.step("Открытие главной страницы"):
            main_page.open()

        with allure.step("Принятие куки"):
            main_page.accept_cookies()

        with allure.step("Клик по логотипу 'Яндекса'"):
            main_page.click_yandex_logo()

        with allure.step("Ожидание и переключение на новое окно"):
            main_page.wait_and_switch_to_new_window()

        with allure.step("Проверка редиректа на Dzen"):
            main_page.wait_for_url_contains(DZEN_REDIRECT_URL)
            assert DZEN_REDIRECT_URL in driver.current_url, \
                f"Expected URL containing {DZEN_REDIRECT_URL}, got {driver.current_url}"

