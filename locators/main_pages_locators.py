from selenium.webdriver.common.by import By

class MainLocators:
    ORDER_BUTTON_1 = (By.XPATH, "//button[text()='Заказать']")
    ORDER_STATUS_TEXT = (By.XPATH, "//button[text()='Статус заказа']")
    ORDER_BUTTON_2 = (By.XPATH, "//div[starts-with(@class, 'Home_FinishButton__')]/button[text()='Заказать']")
    COOKIE_CONFIRM_BUTTON = (By.XPATH, "//button[@id='rcc-confirm-button']")
    IMPORTANT_QUESTION_TEXT = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Локаторы вопросов по ID (самый стабильный вариант для Яндекс.Самоката)
    IMPORTANT_QUESTION_1 = (By.XPATH, "//div[@id='accordion_heading-0']")
    IMPORTANT_QUESTION_2 = (By.XPATH, "//div[@id='accordion_heading-1']")
    IMPORTANT_QUESTION_3 = (By.XPATH, "//div[@id='accordion_heading-2']")
    IMPORTANT_QUESTION_4 = (By.XPATH, "//div[@id='accordion_heading-3']")
    IMPORTANT_QUESTION_5 = (By.XPATH, "//div[@id='accordion_heading-4']")
    IMPORTANT_QUESTION_6 = (By.XPATH, "//div[@id='accordion_heading-5']")
    IMPORTANT_QUESTION_7 = (By.XPATH, "//div[@id='accordion_heading-6']")
    IMPORTANT_QUESTION_8 = (By.XPATH, "//div[@id='accordion_heading-7']")

    # Локаторы ответов по ID
    IMPORTANT_ANSWER_1 = (By.XPATH, "//div[@id='accordion_panel-0']/p")
    IMPORTANT_ANSWER_2 = (By.XPATH, "//div[@id='accordion_panel-1']/p")
    IMPORTANT_ANSWER_3 = (By.XPATH, "//div[@id='accordion_panel-2']/p")
    IMPORTANT_ANSWER_4 = (By.XPATH, "//div[@id='accordion_panel-3']/p")
    IMPORTANT_ANSWER_5 = (By.XPATH, "//div[@id='accordion_panel-4']/p")
    IMPORTANT_ANSWER_6 = (By.XPATH, "//div[@id='accordion_panel-5']/p")
    IMPORTANT_ANSWER_7 = (By.XPATH, "//div[@id='accordion_panel-6']/p")
    IMPORTANT_ANSWER_8 = (By.XPATH, "//div[@id='accordion_panel-7']/p")

