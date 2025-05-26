from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from all_locators import MainPageLocators
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

    @allure.step('Открывает базовый URL.')
    def open(self):
        self.driver.get(self.base_url)

    @allure.step('Находит элемент по локатору с явным ожиданием.')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Находит список элементов по локатору с явным ожиданием.')
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Кликает по элементу по локатору с явным ожиданием.')
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

    @allure.step('Вводит текст в элемент по локатору с явным ожиданием.')
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

    @allure.step('Принимает куки, если баннер присутствует.')
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BANNER)
        except Exception:
            pass

    @allure.step('Прокрутка экрана до элемента.')
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find_element(locator))

    @allure.step('Получает текст элемента.')
    def get_element_text(self, locator, timeout=10):
        return self.find_element(locator, timeout).text

    @allure.step('Проверяет, отображается ли элемент.')
    def is_element_displayed(self, locator, timeout=10):
        try:
            return self.find_element(locator, timeout).is_displayed()
        except TimeoutException:
            return False

    @allure.step('Ожидание и клик по элементу')
    def wait_and_click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    @allure.step('Ожидание, что URL содержит "{url_part}"')
    def wait_for_url_contains(self, url_part, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(url_part)
        )

    @allure.step('Ожидание и переключение на новое окно')
    def wait_and_switch_to_new_window(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.window_handles) > 1
        )
        self.driver.switch_to.window(self.driver.window_handles[1])



####

