from selenium.webdriver.common.by import By
from .Pages.main_page import MainPage
from .Pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    # login_page.should_be_login_url()
    # login_page.should_be_login_page()
    # login_page.should_be_register_form()

    browser.get(link)
    go_to_login_page(browser)


def go_to_login_page(browser):
    login_link = browser.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


# start command 'pytest -v --tb=line --language=en test_main_page.py'