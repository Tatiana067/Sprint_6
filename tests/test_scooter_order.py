import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from url import MAIN_URL, DZEN
from locators.order_pages_locators import RentalFormLocators

# Тестовые данные для сквозного сценария
ORDER_TEST_DATA = [
    (
        "top", 
        "Иван", 
        "Петров", 
        "ул. Ленина, д. 10", 
        "Преображенская площадь", 
        "+79991112233", 
        "25.10.2026", 
        "сутки", 
        RentalFormLocators.BLACK_COLOR_CHECKBOX, 
        "Позвонить курьеру заранее"
    ),
    (
        "bottom", 
        "Анна", 
        "Смирнова", 
        "проспект Мира, д. 5, кв. 12", 
        "Сокольники", 
        "89115556677", 
        "26.10.2026", 
        "двое суток", 
        RentalFormLocators.GREY_COLOR_CHECKBOX, 
        "Оставить у двери"
    )
]


@allure.title('Parametrized test: Сквозной сценарий заказа самоката и проверка логотипов')
@pytest.mark.parametrize(
    "button_type, name, surname, address, metro, phone, date, duration, color_locator, comment",
    ORDER_TEST_DATA
)
def test_order_flow(main_page, order_page, button_type, name, surname, address, metro, phone, date, duration, color_locator, comment):
    # 1. Открываем главную страницу
    main_page.open_main_page()
    
    try:
        main_page.accept_cookies()
    except Exception:
        pass

    driver = main_page.driver

    # Выбор и клик по кнопке заказа в зависимости от параметра
    if button_type == "top":
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RentalFormLocators.ORDER_BUTTON_1)
        ).click()
    else:
        # Автоматический нативный клик со встроенным скроллом от Selenium
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RentalFormLocators.ORDER_BUTTON_2)
        ).click()

    # Заполнение первой и второй форм заказа
    order_page.fill_order_form(
        name=name, 
        surname=surname, 
        address=address, 
        metro_name=metro, 
        phone=phone
    )
    order_page.fill_rental_form(
        date_text=date, 
        duration_text=duration, 
        color_checkbox_locator=color_locator, 
        comment=comment
    )
    order_page.confirm_order()

    # Проверка модального окна успешного заказа
    assert order_page.is_order_placed_modal_displayed(), "Окно 'Заказ оформлен' не появилось!"

    # Проверка клика по логотипу "Самокат"
    order_page.click_scooter_logo()
    assert MAIN_URL in order_page.driver.current_url, (
        f"Логотип не вернул на главную. Текущий URL: {order_page.driver.current_url}"
    )

    # Проверка клика по логотипу "Яндекс" и перехода на Дзен
    order_page.click_yandex_logo()
    current_dzen_url = order_page.switch_to_dzen_tab()
    assert DZEN in current_dzen_url, (
        f"Редирект на Дзен не сработал. Текущий URL: {current_dzen_url}"
    )



