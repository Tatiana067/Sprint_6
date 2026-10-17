import pytest
import allure
from locators.main_pages_locators import MainLocators

@allure.title('Проверка Вопроса №1')
def test_important_question_1(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_1)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_1)
    
    assert actual_text == 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

@allure.title('Проверка Вопроса №2')
def test_important_question_2(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_2)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_2)
    
    assert actual_text == 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

@allure.title('Проверка Вопроса №3')
def test_important_question_3(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_3)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_3)
    
    assert actual_text == 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

@allure.title('Проверка Вопроса №4')
def test_important_question_4(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_4)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_4)
    
    assert actual_text == 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

@allure.title('Проверка Вопроса №5')
def test_important_question_5(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_5)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_5)
    
    assert actual_text == 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

@allure.title('Проверка Вопроса №6')
def test_important_question_6(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_6)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_6)
    
    assert actual_text == 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

@allure.title('Проверка Вопроса №7')
def test_important_question_7(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_7)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_7)
    
    assert actual_text == 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

@allure.title('Проверка Вопроса №8')
def test_important_question_8(main_page):
    main_page.open_main_page()
    main_page.accept_cookies()
    
    main_page.click_question(MainLocators.IMPORTANT_QUESTION_8)
    actual_text = main_page.get_answer_text(MainLocators.IMPORTANT_ANSWER_8)
    
    assert actual_text == 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
