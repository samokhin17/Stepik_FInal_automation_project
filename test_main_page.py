from selenium.webdriver.common.by import By
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()



# start command 'pytest -v --tb=line --language=en test_main_page.py'