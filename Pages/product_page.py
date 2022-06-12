from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.webdriver.common.by import By

class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.BASKET)
        basket.click()

    def should_be_correct_name(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text == self.browser.find_element(*ProductPageLocators.BOOK_NAME).text, 'Book name is different'

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BOOK_PRICE).text == self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text, 'Book price is different'
