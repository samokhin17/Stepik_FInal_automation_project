from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        basket.click()

    def should_be_correct_name(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BOOK_NAME).text == self.browser.find_element(
            *ProductPageLocators.BOOK_NAME).text, 'Book name is different'

    def should_be_correct_price(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_BOOK_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BOOK_PRICE).text, 'Book price is different'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Element is still presented, but should not be"
