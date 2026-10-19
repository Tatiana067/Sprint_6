# pages\base_pages.py
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import BASE_URL
from locators.base_pages_locators import BaseLocators

TIMEOUT = 10

class BasePage:
    def __init__(self, driver):
        self._driver = driver

    def _wait_visible(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(EC.visibility_of_element_located(locator))

    def _wait_presence(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(EC.presence_of_element_located(locator))

    def _wait_clickable(self, locator, timeout=TIMEOUT):
        return WebDriverWait(self._driver, timeout).until(EC.element_to_be_clickable(locator))

    def _click(self, locator, timeout=TIMEOUT):
        self._wait_clickable(locator, timeout).click()

    def _send_keys(self, locator, text, timeout=TIMEOUT):
        element = self._wait_visible(locator, timeout)
        element.send_keys(text)

    def _scroll_into_view(self, locator, timeout=TIMEOUT):
        element = self._wait_presence(locator, timeout)
        self._driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def _get_text(self, locator, timeout=TIMEOUT):
        element = self._wait_presence(locator, timeout)
        return element.text

    @allure.step('Открыть главную страницу Самоката')
    def open_main_page(self):
        self._driver.get(BASE_URL)

    @allure.step('Кликнуть на кнопку Заказать вверху страницы')
    def click_top_order_button(self):
        self._click(BaseLocators.ORDER_BUTTON_1)

    @allure.step('Кликнуть на кнопку Статус заказа')
    def click_order_status_button(self):
        self._click(BaseLocators.ORDER_STATUS_TEXT)

    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        self._click(BaseLocators.LOGO_SCOOTER)

    @allure.step('Кликнуть на логотип Яндекс')
    def click_yandex_logo(self):
        self._click(BaseLocators.LOGO_YANDEX)

    @allure.step('Переключиться на открывшуюся вкладку Дзена')
    def switch_to_dzen_tab(self):
        WebDriverWait(self._driver, TIMEOUT).until(EC.number_of_windows_to_be(2))

        self._driver.switch_to.window(self._driver.window_handles[-1])

        WebDriverWait(self._driver, 20).until(EC.url_contains('dzen.ru'))

        return self._driver.current_url

    @allure.step('Проверить отображение логотипа Самоката')
    def is_logo_scooter_displayed(self):
        element = self._wait_visible(BaseLocators.LOGO_SCOOTER)
        return element.is_displayed()
