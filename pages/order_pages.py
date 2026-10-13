import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_pages_locators import OrderLocators, RentalFormLocators, PopUpWindowLocators, OrderPlacedWindowLocators
from locators.main_pages_locators import MainLocators

TIMEOUT = 10

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Заполнить первую часть формы Для кого самокат')
    def fill_order_form(self, name, surname, address, metro_name, phone):
        # Ждем загрузки формы
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(OrderLocators.PAGE_ORDER))
        
        # Заполняем текстовые поля
        self.driver.find_element(*OrderLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(*OrderLocators.LAST_NAME_FIELD).send_keys(surname)
        self.driver.find_element(*OrderLocators.ADDRESS_FIELD).send_keys(address)
        
        # Выбор метро через нативный ввод и клик по результату фильтрации
        metro_input = self.driver.find_element(*OrderLocators.METRO_FIELD)
        metro_input.click()
        metro_input.send_keys(metro_name)
        
        # Ждем появления отфильтрованной строки и кликаем на неё нативным методом Python
        metro_item = WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable(OrderLocators.METRO_DROPDOWN_ITEM)
        )
        metro_item.click()

        # Вводим телефон и переходим дальше
        self.driver.find_element(*OrderLocators.PHONE_FIELD).send_keys(phone)
        self.driver.find_element(*OrderLocators.NEXT_BUTTON).click()

    @allure.step('Заполнить вторую часть формы Про аренду')
    def fill_rental_form(self, date_text, duration_text, color_checkbox_locator, comment):
        # Ждем появления поля даты и заполняем его
        date_field = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(RentalFormLocators.WHEN_DELIVER_SCOOTER_FIELD)
        )
        date_field.send_keys(date_text)
        date_field.send_keys(Keys.ENTER)

        # Открываем выпадающий список сроков аренды
        self.driver.find_element(*RentalFormLocators.RENTAL_PERIOD_FIELD).click()
        
        # ИСПРАВЛЕНО: Локатор сужен до выпадающего меню, чтобы не находить скрытые элементы
        duration_xpath = f"//div[contains(@class, 'Dropdown-menu')]//div[text()='{duration_text}']"
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.element_to_be_clickable((By.XPATH, duration_xpath))
        ).click()

        # Выбираем чекбокс цвета, пишем комментарий и жмем "Заказать"
        self.driver.find_element(*color_checkbox_locator).click()
        self.driver.find_element(*RentalFormLocators.COMMENT_COURIER_FIELD).send_keys(comment)
        self.driver.find_element(*OrderLocators.ORDER_BUTTON).click()

    @allure.step('Подтвердить заказ в модальном окне')
    def confirm_order(self):
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(PopUpWindowLocators.ORDER_MODUL_WINDOW))
        self.driver.find_element(*PopUpWindowLocators.YES_BUTTON).click()

    @allure.step('Проверить, что появилось окно Заказ оформлен')
    def is_order_placed_modal_displayed(self):
        element = WebDriverWait(self.driver, TIMEOUT).until(
            EC.visibility_of_element_located(OrderPlacedWindowLocators.ORDER_PLACE_WINDOW)
        )
        return element.is_displayed()

    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(MainLocators.LOGO_SCOOTER)).click()

    @allure.step('Кликнуть на logo Яндекс')
    def click_yandex_logo(self):
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(MainLocators.LOGO_YANDEX)).click()

    @allure.step('Переключиться на открывшуюся вкладку Дзена')
    def switch_to_dzen_tab(self):
        WebDriverWait(self.driver, TIMEOUT).until(lambda d: len(d.window_handles) > 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        # ИСПРАВЛЕНО: Таймаут ожидания загрузки Дзена в Firefox увеличен до 20 секунд
        WebDriverWait(self.driver, 20).until(EC.url_contains("dzen.ru"))
        return self.driver.current_url


