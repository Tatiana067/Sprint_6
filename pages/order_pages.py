import allure
from selenium.webdriver.common.keys import Keys
from pages.base_pages import BasePage
from locators.order_pages_locators import (OrderLocators, RentalFormLocators, PopUpWindowLocators, OrderPlacedWindowLocators)

class OrderPage(BasePage):

    @allure.step('Заполнить форму Для кого самокат')
    def fill_order_form(self, name, lastname, address, metro_name, phone):
        self._wait_visible(OrderLocators.PAGE_ORDER)
        self._send_keys(OrderLocators.NAME_FIELD, name)
        self._send_keys(OrderLocators.LAST_NAME_FIELD, lastname)
        self._send_keys(OrderLocators.ADDRESS_FIELD, address)

        self._click(OrderLocators.METRO_FIELD)
        self._send_keys(OrderLocators.METRO_FIELD, metro_name)

        metro_xpath = OrderLocators.METRO_ITEM_TEMPLATE.format(metro_name)
        self._click(("xpath", metro_xpath))

        self._send_keys(OrderLocators.PHONE_FIELD, phone)
        self._click(OrderLocators.NEXT_BUTTON)

    @allure.step('Заполнить форму Про аренду')
    def fill_rental_form(self, date_text, duration_text, color_checkbox, comment):
        self._send_keys(RentalFormLocators.WHEN_DELIVER_SCOOTER_FIELD, date_text)
        self._send_keys(RentalFormLocators.WHEN_DELIVER_SCOOTER_FIELD, Keys.ENTER)

        self._click(RentalFormLocators.RENTAL_HEADER)
        self._click(RentalFormLocators.RENTAL_PERIOD_FIELD)

        rental_xpath = RentalFormLocators.RENTAL_OPTION_TEMPLATE.format(duration_text)
        self._click(("xpath", rental_xpath))


        self._click(color_checkbox)
        self._send_keys(RentalFormLocators.COMMENT_COURIER_FIELD, comment)
        self._click(OrderLocators.ORDER_BUTTON)

    @allure.step('Подтвердить заказ в модальном окне')
    def confirm_order(self):
        self._wait_visible(PopUpWindowLocators.ORDER_MODUL_WINDOW)
        self._click(PopUpWindowLocators.YES_BUTTON)

    @allure.step('Проверить, что появилось окно Заказ оформлен')
    def is_order_placed_modal_displayed(self):
        self._wait_visible(OrderPlacedWindowLocators.ORDER_PLACE_WINDOW)
        return True

    @allure.step('Кликнуть на кнопку Посмотреть статус')
    def click_show_status_button(self):
        self._click(OrderPlacedWindowLocators.SHOW_STATUS_BUTTON)
