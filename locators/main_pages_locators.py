from selenium.webdriver.common.by import By

class MainLocators: # Главная страница Самоката
    ORDER_BUTTON_1 = (By.XPATH, "//button[text()='Заказать']")
    ORDER_STATUS_TEXT = (By.XPATH, "//button[text()='Статус заказа']")
    ORDER_BUTTON_2 = (By.XPATH, "//div[starts-with(@class, 'Home_FinishButton__')]/button[text()='Заказать']")
    COOKIE_CONFIRM_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")
    IMPORTANT_QUESTION_TEXT = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Локаторы вопросов
    IMPORTANT_QUESTION_1 = (By.ID, "accordion__heading-0")
    IMPORTANT_QUESTION_2 = (By.ID, "accordion__heading-1")
    IMPORTANT_QUESTION_3 = (By.ID, "accordion__heading-2")
    IMPORTANT_QUESTION_4 = (By.ID, "accordion__heading-3")
    IMPORTANT_QUESTION_5 = (By.ID, "accordion__heading-4")
    IMPORTANT_QUESTION_6 = (By.ID, "accordion__heading-5")
    IMPORTANT_QUESTION_7 = (By.ID, "accordion__heading-6")
    IMPORTANT_QUESTION_8 = (By.ID, "accordion__heading-7")

    # Локаторы ответов
    IMPORTANT_ANSWER_1 = (By.ID, "accordion__panel-0")
    IMPORTANT_ANSWER_2 = (By.ID, "accordion__panel-1")
    IMPORTANT_ANSWER_3 = (By.ID, "accordion__panel-2")
    IMPORTANT_ANSWER_4 = (By.ID, "accordion__panel-3")
    IMPORTANT_ANSWER_5 = (By.ID, "accordion__panel-4")
    IMPORTANT_ANSWER_6 = (By.ID, "accordion__panel-5")
    IMPORTANT_ANSWER_7 = (By.ID, "accordion__panel-6")
    IMPORTANT_ANSWER_8 = (By.ID, "accordion__panel-7")


