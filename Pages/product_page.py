from selenium.webdriver.common.by import By
from base_page import BasePage
from locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.BASKET).click()