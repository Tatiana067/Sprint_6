import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from url import MAIN_URL, DZEN
from locators.order_pages_locators import RentalFormLocators
from locators.base_pages_locators import BaseLocators


ORDER_TEST_DATA = [
    ('top', 'Иван', 'Петров', 'ул. Ленина, д. 10', 'Преображенская площадь', '89991112233', '25.10.2026', 'сутки', RentalFormLocators.BLACK_COLOR_CHECKBOX, 'Доставить в 10.00'),
    ('bottom', 'Анна', 'Смирнова', 'проспект Мира, д. 5', 'Сокольники', '89115556677', '26.10.2026', 'двое суток', RentalFormLocators.GREY_COLOR_CHECKBOX, 'Третий подъезд')
]

@allure.title('Заказ самоката с двумя наборами данных')
@pytest.mark.parametrize('button_type, name, lastname, address, metro, phone, date, duration, color_locator, comment', ORDER_TEST_DATA) 
def test_order_flow(main_page, order_page, button_type, name, lastname, address, metro, phone, date, duration, color_locator, comment):
    main_page.open_main_page()
    
    try:
        main_page.accept_cookies()
    except Exception:
        pass

    driver = main_page.driver

    if button_type == 'top':
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RentalFormLocators.ORDER_BUTTON_1)).click()
    else:
        button_2 = WebDriverWait(driver, 10).until(EC.presence_of_element_located(RentalFormLocators.ORDER_BUTTON_2))
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button_2)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(RentalFormLocators.ORDER_BUTTON_2)).click()

    order_page.fill_order_form(name=name, lastname=lastname, address=address, metro_name=metro, phone=phone)
    order_page.fill_rental_form(date_text=date, duration_text=duration, color_checkbox=color_locator, comment=comment)
    order_page.confirm_order()

    assert order_page.is_order_placed_modal_displayed(), "Окно 'Заказ оформлен' не появилось!"

    order_page.click_scooter_logo()
    WebDriverWait(driver, 10).until(EC.url_contains(MAIN_URL))
    assert MAIN_URL in driver.current_url, f"Логотип не вернул на главную. Текущий URL: {driver.current_url}"

    order_page.click_yandex_logo()
    
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
    
    current_dzen_url = order_page.switch_to_dzen_tab()
    
    assert DZEN in current_dzen_url, f"Редирект на Дзен не сработал. Текущий URL: {current_dzen_url}"


