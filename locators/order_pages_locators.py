from selenium.webdriver.common.by import By

class OrderLocators:
    PAGE_ORDER = (By.XPATH, "//*[contains(text(), 'Для кого самокат')]")
    NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Имя')]")
    LAST_NAME_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Фамилия')]")
    ADDRESS_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Адрес')]")
    METRO_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Станция метро')]")
    
    
    METRO_DROPDOWN_ITEM = (By.XPATH, "//div[contains(@class, 'select-search__select')]//button")
    
    PHONE_FIELD = (By.XPATH, "//input[contains(@placeholder, 'Телефон')]")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Заказать']")


class RentalFormLocators: # страница с формой Про аренду
    WHEN_DELIVER_SCOOTER_FIELD = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD_FIELD = (By.XPATH, "//div[text()='* Срок аренды']")
    DROP_DOWN_LIST = (By.XPATH, "//span[@class='Dropdown-arrow']")
    COLOR_SCOOTER_FIELD = (By.XPATH, "//div[text()='Цвет самоката']")
    BLACK_COLOR_CHECKBOX = (By.ID, "black")
    GREY_COLOR_CHECKBOX = (By.ID, "grey")
    COMMENT_COURIER_FIELD = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    BACK_BUTTON = (By.XPATH, "//button[text()='Назад']")
    ORDER_BUTTON_1 = (By.XPATH, "//div[contains(@class, 'Header_Nav')]//button[text()='Заказать']")
    ORDER_BUTTON_2 = (By.XPATH, "//div[contains(@class, 'Home_ThirdPart')]//button[text()='Заказать']") # Обновленный селектор нижнего блока

class PopUpWindowLocators: # всплывающее окно подтверждения
    ORDER_MODUL_WINDOW = (By.XPATH, "//div[starts-with(@class, 'Order_ModalHeader__')]")
    YES_BUTTON = (By.XPATH, "//button[text()='Да']")
    NOT_BUTTON = (By.XPATH, "//button[text()='Нет']")

class OrderPlacedWindowLocators: 
    ORDER_PLACE_WINDOW = (By.XPATH, "//div[text()='Заказ оформлен']")
