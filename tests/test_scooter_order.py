import pytest
import allure
from locators.main_pages_locators import MainLocators
from locators.base_pages_locators import BaseLocators
from url import DZEN
from data import ORDER_TEST_DATA

class TestScooterOrderFlow:

    @allure.title('Заказ самоката с двумя наборами данных')
    @pytest.mark.parametrize('button_type, name, lastname, address, metro, phone, date, duration, color_locator, comment',ORDER_TEST_DATA,)
    def test_order_flow_and_header_logos(self, main_page, order_page, button_type, name, lastname, address, metro, phone, date, duration, color_locator, comment,):
        main_page.open_main_page()
        main_page.accept_cookies()

        order_buttons = {'top': BaseLocators.ORDER_BUTTON_1, 'bottom': MainLocators.ORDER_BUTTON_2,}
        target_button = order_buttons[button_type]

        main_page._scroll_into_view(target_button)
        main_page._click(target_button)

        order_page.fill_order_form(name, lastname, address, metro, phone)
        order_page.fill_rental_form(date, duration, color_locator, comment)
        order_page.confirm_order()

        assert (order_page.is_order_placed_modal_displayed()), 'Окно Заказ оформлен не появилось!'

        order_page.click_show_status_button()

        order_page.click_scooter_logo()
        assert (order_page.is_logo_scooter_displayed()), 'Клик по логотипу Самоката не вернул пользователя на главную страницу!'

        order_page.click_yandex_logo()
        current_dzen_url = order_page.switch_to_dzen_tab()

        assert (DZEN in current_dzen_url), f'Редирект на Дзен не сработал. Текущий URL: {current_dzen_url}'
