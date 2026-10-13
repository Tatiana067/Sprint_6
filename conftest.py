import pytest
from selenium import webdriver
# ИСПРАВЛЕНО: импортируем из main_pages, а не из base_pages
from pages.main_pages import MainPage 
from pages.order_pages import OrderPage

@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.set_window_size(1920, 1080)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    return MainPage(driver)

@pytest.fixture
def order_page(driver):
    return OrderPage(driver)
