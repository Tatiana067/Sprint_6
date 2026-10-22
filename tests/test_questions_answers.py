import pytest
import allure
from locators.main_pages_locators import MainLocators
from data import ACCORDION_DATA

class TestMainPageAccordion:

    @allure.title('Проверка соответствия ответов на вопросы')
    @pytest.mark.parametrize('index', range(len(ACCORDION_DATA)))
    def test_important_questions_and_answers(self, main_page, index):
        
        question_locator = getattr(MainLocators, f'IMPORTANT_QUESTION_{index + 1}')
        answer_locator = getattr(MainLocators, f'IMPORTANT_ANSWER_{index + 1}')

        main_page.open_main_page()
        main_page.accept_cookies()

        main_page.click_question(question_locator)
        actual_text = main_page.get_answer_text(answer_locator)

        expected_text = ACCORDION_DATA[index]['answer']
        assert (actual_text == expected_text), f"Текст ответа не совпадает. Ожидалось: '{expected_text}', Получено: '{actual_text}'"
