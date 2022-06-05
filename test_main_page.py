from selenium.webdriver.common.by import By
from .Pages.main_page import MainPage

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
<<<<<<< HEAD
    page = MainPage(browser, link)
    page.open()
    # page.go_to_login_page()
    page.should_be_login_link()
=======
    browser.get(link)
    go_to_login_page(browser)


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()
>>>>>>> 7bbb6b37df8a938f5aac60b59971bce0a8bc3e98

# start command 'pytest -v --tb=line --language=en test_main_page.py'