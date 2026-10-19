from selenium.webdriver.common.by import By

class OrderLocators: # Страница с формой Для кого самокат
    PAGE_ORDER = (By.XPATH, "//*[contains(text(), 'Для кого самокат')]")
    NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")
    METRO_ITEM_TEMPLATE = "//div[contains(@class, 'select-search__select')]//button[contains(., '{0}')]"

class RentalFormLocators: # Страница с формой Про аренду
    RENTAL_HEADER = (By.XPATH, "//div[contains(text(), 'Про аренду')]")
    WHEN_DELIVER_SCOOTER_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    DROP_DOWN_LIST = (By.XPATH, "//span[@class='Dropdown-arrow']")
    COLOR_SCOOTER_FIELD = (By.XPATH, "//div[text()='Цвет самоката']")
    BLACK_COLOR_CHECKBOX = (By.XPATH, "//label[@for='black']")
    GREY_COLOR_CHECKBOX = (By.XPATH, "//label[@for='grey']")
    COMMENT_COURIER_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, "//button[text()='Назад']")
    RENTAL_OPTION_TEMPLATE = "//div[contains(@class, 'Dropdown-menu')]//div[text()='{0}']"

class PopUpWindowLocators: # Всплывающее окно подтверждения
    ORDER_MODUL_WINDOW = (By.XPATH, "//div[contains(text(), 'Хотите оформить заказ?')]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NOT_BUTTON = (By.XPATH, "//button[text()='Нет']")


class OrderPlacedWindowLocators: # Всплывающее окно Заказ оформлен
    ORDER_PLACE_WINDOW = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader')]")
    SHOW_STATUS_BUTTON = (By.XPATH, "//button[text()='Посмотреть статус']")
