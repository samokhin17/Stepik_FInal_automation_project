from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def should_not_be_a_supply(self):
        assert self.is_not_element_present(*BasketPageLocators.SUPPLY), "Supply mustn't be"

    def should_be_a_basket_free_text(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_FREE), "There is no basket free text"
        assert True