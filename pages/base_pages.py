import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import BASE_URL
from locators.base_pages_locators import BaseLocators

TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self.driver = driver

class MainPage(BasePage):

    @allure.step('Открыть главную страницу Самоката')
    def open_main_page(self):
        self.driver.get(BASE_URL)

    @allure.step("Проверить наличие логотипа 'Самокат'")
    def is_logo_scooter_displayed(self):
        # Метод wait возвращает элемент, когда он становится видимым
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(BaseLocators.LOGO_SCOOTER)
        )
        return element

