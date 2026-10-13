import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from url import BASE_URL
from locators.main_pages_locators import MainLocators
from pages.base_pages import BasePage

TIMEOUT = 15

class MainPage(BasePage):

    @allure.step('Открыть главную страницу Самоката')
    def open_main_page(self):
        self.driver.get(BASE_URL)

    @allure.step('Принять файлы cookie')
    def accept_cookies(self):
        try:
            cookie_btn = WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable(MainLocators.COOKIE_CONFIRM_BUTTON)
            )
            cookie_btn.click()
        except Exception:
            pass

    @allure.step('Кликнуть на вопрос')
    def click_question(self, question):
        # Находим элемент по его тексту в DOM-структуре
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(question)
        )
        # Нативный Python-скролл к элементу и клик по нему
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click(element).perform()

    @allure.step('Получить текст ответа')
    def get_answer_text(self, answer):
        # Ожидаем появление текста ответа в DOM
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located(answer)
        )
        return element.text




