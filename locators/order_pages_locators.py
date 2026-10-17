from selenium.webdriver.common.by import By

class OrderLocators: # страница с фомой Для кого самокат
    PAGE_ORDER = (By.XPATH, "//*[contains(text(), 'Для кого самокат')]")
    NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    METRO_DROPDOWN_ITEM = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button[contains(., '{}')]")
    PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons__')]/button[text()='Заказать']")

class RentalFormLocators: # страница с формой Про аренду
    WHEN_DELIVER_SCOOTER_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    RENTAL_OPTION_TEMPLATE = (By.XPATH, "//div[contains(@class, 'Dropdown-menu')]//div[text()='{}']")
    DROP_DOWN_LIST = (By.XPATH, "//span[@class='Dropdown-arrow']")
    COLOR_SCOOTER_FIELD = (By.XPATH, "//div[text()='Цвет самоката']")
    BLACK_COLOR_CHECKBOX = (By.XPATH, "//label[@for='black']")
    GREY_COLOR_CHECKBOX = (By.XPATH, "//label[@for='grey']")
    COMMENT_COURIER_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, "//button[text()='Назад']")
    ORDER_BUTTON_1 = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_2 = (By.XPATH, "//div[contains(@class, 'Home_ThirdPart')]//button[text()='Заказать']")
    RENTAL_HEADER = (By.XPATH, "//div[contains(text(), 'Про аренду')]")

class PopUpWindowLocators: # всплывающее окно подтверждения
    ORDER_MODUL_WINDOW = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NOT_BUTTON = (By.XPATH, "//button[text()='Нет']")

class OrderPlacedWindowLocators: # всплывающее окно Заказ оформлен
    ORDER_PLACE_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    SHOW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
