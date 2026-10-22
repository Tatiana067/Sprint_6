from selenium.webdriver.common.by import By

class BaseLocators: # Базовая страница Самоката
    LOGO_YANDEX = (By.XPATH, "//img[@alt='Yandex']")  # логотип Яндекс
    LOGO_SCOOTER = (By.XPATH, "//img[@alt='Scooter']")  # логотип Самокат
    ORDER_BUTTON_1 = (By.XPATH, "//button[text()='Заказать']")  # кнопка Заказать
    ORDER_STATUS_TEXT = (By.XPATH, "//*[text()='Статус заказа']")  # текст Статус заказа
