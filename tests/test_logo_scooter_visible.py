import allure
# Исправлено: импортируем MainPage вместо BasePage
from pages.base_pages import MainPage

@allure.title('Проверка отображения логотипа Самоката')
def test_logo_scooter_is_visible(driver):
    
    # Исправлено: инициализируем класс главной страницы
    main_page = MainPage(driver)
    
    main_page.open_main_page()
    
    is_displayed = main_page.is_logo_scooter_displayed()
    
    assert is_displayed, 'Логотип Самоката должен быть виден на главной странице, но он не отображается!'

