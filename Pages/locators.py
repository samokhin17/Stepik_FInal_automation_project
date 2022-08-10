from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = (By.ID, "login_link")
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_FORM = (By.ID, 'register_form')
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_REPEAT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_BUTTON = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, '#add_to_basket_form [type="submit"]')
    BOOK_NAME = (By.CSS_SELECTOR, 'li.active:nth-child(5)')
    BOOK_PRICE = (By.CSS_SELECTOR, 'p.price_color:nth-child(2)')
    BASKET_BOOK_NAME = (By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2) > strong:nth-child(1)')
    BASKET_BOOK_PRICE = (
    By.CSS_SELECTOR, 'div.alert:nth-child(3) > div:nth-child(2) > p:nth-child(1) > strong:nth-child(1)')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'div.alert:nth-child(1) > div:nth-child(2)')


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET = (By.CSS_SELECTOR, ".btn-group > a:nth-child(1)")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    SUPPLY = (By.CSS_SELECTOR, ".basket-items > div:nth-child(1)")
    BASKET_FREE = (By.CSS_SELECTOR, "#content_inner > p:nth-child(1)")
