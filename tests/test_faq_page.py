import allure
import pytest

from data import FAQ_DATA
from pages.faq_page import FAQPage


@allure.feature('Тесты раздела FAQ')
class TestFAQPage:
    @allure.title('Проверка текста вопросов')
    @pytest.mark.parametrize('question_num', list(FAQ_DATA.keys()))
    def test_question_text(self, driver, question_num):
        """Проверяет соответствие текста вопросов ожидаемым данным."""
        faq_page = FAQPage(driver)
        faq_page.open()
        faq_page.accept_cookies()
        faq_page.scroll_to_faq_section()

        question_text = faq_page.get_question_text(question_num)
        assert question_text == FAQ_DATA[question_num]['question'], \
            f"Текст вопроса №{question_num} не совпадает с ожидаемым"

    @allure.title('Проверка работы аккордеона')
    @pytest.mark.parametrize('question_num', list(FAQ_DATA.keys()))
    def test_accordion_behavior(self, driver, question_num):
        """Проверяет, что при клике на вопрос появляется правильный ответ."""
        faq_page = FAQPage(driver)
        faq_page.open()
        faq_page.accept_cookies()
        faq_page.scroll_to_faq_section()

        # Проверяем начальное состояние
        initial_state = faq_page.is_answer_displayed(question_num)

        # Кликаем на вопрос
        faq_page.click_question(question_num)

        # Проверяем изменение состояния
        assert faq_page.is_answer_displayed(question_num) != initial_state, \
            "Состояние ответа не изменилось после клика"

        # Проверяем текст ответа
        answer_text = faq_page.get_answer_text(question_num)
        assert answer_text == FAQ_DATA[question_num]['answer'], \
            f"Текст ответа на вопрос №{question_num} не совпадает с ожидаемым"