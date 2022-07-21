from selenium.webdriver.common.by import By
import pytest
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage
from .Pages.basket_page import BasketPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

@pytest.mark.new
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = BasketPage(browser, link)
    page.open()
    page.open_basket_page()
    page.should_not_be_a_supply()
    page.should_be_a_basket_free_text()

# start command 'pytest -v --tb=line --language=en test_main_page.py'