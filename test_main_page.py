from selenium.webdriver.common.by import By
from .Pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    # page.go_to_login_page()
    page.should_be_login_link()

    




# start command 'pytest -v --tb=line --language=en test_main_page.py'