from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from all_locators import MainPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = "https://qa-scooter.praktikum-services.ru/"

# Открывает базовый URL
    def open(self):
        self.driver.get(self.base_url)

# Находит элемент по локатору с явным ожиданием
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

# Находит список элементов по локатору с явным ожиданием
    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

# Кликает по элементу по локатору с явным ожиданием
    def click_element(self, locator, timeout=10):
        element = self.find_element(locator, timeout)
        element.click()

# Вводит текст в элемент по локатору с явным ожиданием
    def send_keys(self, locator, text, timeout=10):
        element = self.find_element(locator, timeout)
        element.clear()
        element.send_keys(text)

# Принимает куки, если баннер присутствует
    def accept_cookies(self):
        try:
            self.click_element(MainPageLocators.COOKIE_BANNER)
        except Exception as e:
            print(f"Ошибка при закрытии баннера куки: {e}")

# Прокрутка экрана до элемента
    def scroll_to_element(self, locator):
        self.driver.execute_script('arguments[0].scrollIntoView();', self.find_element(locator))





####

