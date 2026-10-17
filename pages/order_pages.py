import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.order_pages_locators import OrderLocators, RentalFormLocators, PopUpWindowLocators, OrderPlacedWindowLocators
from locators.base_pages_locators import BaseLocators
from pages.base_pages import BasePage

TIMEOUT = 10

class OrderPage(BasePage):

    @allure.step('Заполнить форму Для кого самокат')
    def fill_order_form(self, name, lastname, address, metro_name, phone):
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(OrderLocators.PAGE_ORDER))

        self.driver.find_element(*OrderLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(*OrderLocators.LAST_NAME_FIELD).send_keys(lastname)
        self.driver.find_element(*OrderLocators.ADDRESS_FIELD).send_keys(address)

        metro_input = self.driver.find_element(*OrderLocators.METRO_FIELD)
        metro_input.click()
        metro_input.send_keys(metro_name)

        by, xpath_template = OrderLocators.METRO_DROPDOWN_ITEM
        dynamic_xpath = xpath_template.format(metro_name)
        
        metro_item = WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable((by, dynamic_xpath)))
        metro_item.click()

        self.driver.find_element(*OrderLocators.PHONE_FIELD).send_keys(phone)
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(OrderLocators.NEXT_BUTTON)).click()

    @allure.step('Заполнить форму Про аренду')
    def fill_rental_form(self, date_text, duration_text, color_checkbox, comment):
        
        date_field = WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(RentalFormLocators.WHEN_DELIVER_SCOOTER_FIELD))
        date_field.send_keys(date_text)
        date_field.send_keys(Keys.ENTER)

        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(RentalFormLocators.RENTAL_HEADER)).click()
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(RentalFormLocators.RENTAL_PERIOD_FIELD)).click()

        by, xpath_template = RentalFormLocators.RENTAL_OPTION_TEMPLATE
        dynamic_xpath = xpath_template.format(duration_text)
        
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable((by, dynamic_xpath))).click()

        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(color_checkbox)).click()
        self.driver.find_element(*RentalFormLocators.COMMENT_COURIER_FIELD).send_keys(comment)
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(OrderLocators.ORDER_BUTTON)).click()


    @allure.step('Подтвердить заказ в модальном окне')
    def confirm_order(self):
        
        WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(PopUpWindowLocators.ORDER_MODUL_WINDOW))
        
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(PopUpWindowLocators.YES_BUTTON)).click()
 
    @allure.step('Проверить, что появилось окно Заказ оформлен')
    def is_order_placed_modal_displayed(self):
        element = WebDriverWait(self.driver, TIMEOUT).until(EC.visibility_of_element_located(OrderPlacedWindowLocators.ORDER_PLACE_WINDOW))
        displayed = element.is_displayed()
        
        if displayed:
            WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(OrderPlacedWindowLocators.SHOW_STATUS_BUTTON)).click()
            
        return displayed
   
    @allure.step('Кликнуть на логотип Самоката')
    def click_scooter_logo(self):
    
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(BaseLocators.LOGO_SCOOTER)).click()

    @allure.step('Кликнуть на logo Яндекс')
    def click_yandex_logo(self):
        
        WebDriverWait(self.driver, TIMEOUT).until(EC.element_to_be_clickable(BaseLocators.LOGO_YANDEX)).click()

    @allure.step('Переключиться на открывшуюся вкладку Дзена')
    def switch_to_dzen_tab(self):
        
        WebDriverWait(self.driver, TIMEOUT).until(lambda d: len(d.window_handles) > 1)
        
        self.driver.switch_to.window(self.driver.window_handles[-1])
        
        WebDriverWait(self.driver, 20).until(EC.url_contains("dzen.ru"))
        
        return self.driver.current_url
