from selenium.webdriver.common.by import By
import allure
from pages.base_page import BasePage
from all_locators import FAQLocators
from urls import MAIN_PAGE_URL, ORDER_PAGE_URL, DZEN_REDIRECT_URL

# Класс для работы с разделом FAQ на главной странице
class FAQPage(BasePage):

    @allure.step('Получить текст вопроса по номеру')
    def get_question_text(self, question_num):
        locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemButton'])[{question_num + 1}]")
        return self.get_element_text(locator)

    @allure.step('Кликнуть по вопросу по номеру')
    def click_question(self, question_num):
        locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemButton'])[{question_num + 1}]")
        self.scroll_to_element(locator)
        self.click_element(locator)

    @allure.step('Получить текст ответа по номеру')
    def get_answer_text(self, question_num):
        locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemPanel'])[{question_num + 1}]")
        return self.get_element_text(locator, timeout=5)

    @allure.step('Проверить отображение ответа по номеру')
    def is_answer_displayed(self, question_num):
        locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemPanel'])[{question_num + 1}]")
        return self.is_element_displayed(locator, timeout=2)

    @allure.step('Прокрутить до раздела FAQ')
    def scroll_to_faq_section(self):
        self.scroll_to_element(FAQLocators.FAQ_SECTION)