# test_logo.py
import pytest
import allure
from pages.main_pages import MainPage

class TestScooterLogo:

    @allure.title('Проверка отображения логотипа Самоката')
    def test_logo_scooter_is_visible(self, main_page):
        main_page.open_main_page()
        is_displayed = main_page.is_logo_scooter_displayed()

        assert is_displayed, 'Логотип Самоката должен быть виден на главной странице, но он не отображается!'
