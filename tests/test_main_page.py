import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from data import DZEN_REDIRECT_URL, MAIN_PAGE_URL


@allure.feature("Main Page")
@allure.story("Redirect to main page after clicking on the scooter logo")
def test_scooter_logo_redirect(driver):
    main_page = MainPage(driver)

    @allure.step("Открытие главной страницы")
    def open_page():
        main_page.open()

    @allure.step("Принятие куки")
    def accept_cookies():
        main_page.accept_cookies()

    @allure.step("Клик по логотипу 'Самоката'")
    def click_logo():
        main_page.click_scooter_logo()

    @allure.step("Проверка редиректа на главную страницу")
    def check_redirect():
        WebDriverWait(driver, 10).until(EC.url_contains(MAIN_PAGE_URL))
        assert MAIN_PAGE_URL in driver.current_url, \
            f"Expected URL containing {MAIN_PAGE_URL}, got {driver.current_url}"

    open_page()
    accept_cookies()
    click_logo()
    check_redirect()


@allure.feature("Main Page")
@allure.story("Redirect to Dzen after clicking on the Yandex logo")
def test_yandex_logo_redirect(driver):
    main_page = MainPage(driver)

    @allure.step("Открытие главной страницы")
    def open_page():
        main_page.open()

    @allure.step("Принятие куки")
    def accept_cookies():
        main_page.accept_cookies()

    @allure.step("Клик по логотипу 'Яндекса'")
    def click_logo():
        main_page.click_yandex_logo()

    @allure.step("Ожидание и переключение на новое окно")
    def switch_window():
        WebDriverWait(driver, 10).until(lambda d: len(d.window_handles) > 1)
        driver.switch_to.window(driver.window_handles[1])

    @allure.step("Проверка редиректа на Dzen")
    def check_redirect():
        # Ожидание, что URL в текущей (новой) вкладке будет содержать DZEN_REDIRECT_URL
        WebDriverWait(driver, 10).until(
            EC.url_contains(DZEN_REDIRECT_URL)
        )
        assert DZEN_REDIRECT_URL in driver.current_url, \
            f"Expected URL containing {DZEN_REDIRECT_URL}, got {driver.current_url}"

    open_page()
    accept_cookies()
    click_logo()
    switch_window()
    check_redirect()