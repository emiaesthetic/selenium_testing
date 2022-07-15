from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_to_basket(self):
        button_basket = self.browser.find_element(*ProductPageLocators.BTN_BASKET)
        button_basket.click()

    def should_be_names_match(self):
        name_book = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_book_in_basket = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_IN_BASKET).text
        assert name_book == name_book_in_basket, "Book titles are different!"

    def should_be_price_match(self):
        price_book = self.browser.find_element(*ProductPageLocators.PRICE_BOOK).text
        price_basket = self.browser.find_element(*ProductPageLocators.PRICE_BASKET).text
        assert price_book == price_basket, "The price is different!"
