import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from all_locators import FAQLocators

# Класс для работы с разделом FAQ на главной странице
class FAQPage(BasePage):

    @allure.step('Получить текст вопроса по номеру')
    # Получает текст вопроса по его номеру
    def get_question_text(self, question_num):
        locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemButton'])[{question_num + 1}]")
        return self.find_element(locator).text

    @allure.step('Кликнуть по вопросу по номеру')
    # Кликает по вопросу по его номеру
    def click_question(self, question_num):
        locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemButton'])[{question_num + 1}]")
        question = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", question)
        question.click()

    @allure.step('Получить текст ответа по номеру')
    # Получает текст ответа по номеру вопроса
    def get_answer_text(self, question_num):
        locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemPanel'])[{question_num + 1}]")
        return self.find_element(locator, timeout=5).text

    @allure.step('Проверить отображение ответа по номеру')
    # Проверяет, отображается ли ответ по номеру вопроса
    def is_answer_displayed(self, question_num):
        try:
            locator = (By.XPATH, f"(//div[@data-accordion-component='AccordionItemPanel'])[{question_num + 1}]")
            return self.find_element(locator, timeout=2).is_displayed()
        except:
            return False

    @allure.step('Прокрутить до раздела FAQ')
    # Прокручивает страницу до раздела FAQ
    def scroll_to_faq_section(self):
        self.scroll_to_element(FAQLocators.FAQ_SECTION)
