import allure
from locators.main_pages_locators import MainLocators
from pages.base_pages import BasePage

class MainPage(BasePage):

    @allure.step('Принять файлы cookie')
    def accept_cookies(self):
        try:
            self._click(MainLocators.COOKIE_CONFIRM_BUTTON, timeout=3)
        except Exception:
            pass

    @allure.step('Кликнуть на вопрос')
    def click_question(self, question):
        self._scroll_into_view(question)
        self._click(question)

    @allure.step('Получить текст ответа')
    def get_answer_text(self, answer):
        return self._get_text(answer)
