from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')

class ProductPageLocators():
    BASKET = (By.CSS_SELECTOR, '#add_to_basket_form [type="submit"]')
    BOOK_NAME = (By.CSS_SELECTOR, 'li.active:nth-child(5)')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color:nth-child(2)')
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    BASKET_BOOK_PRICE = (By.CSS_SELECTOR, 'div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)')