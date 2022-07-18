from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_basket_page(self):
        self.should_not_be_basket_items()
        self.should_be_message_basket_empty()

    def should_not_be_basket_items(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Your basket items is not empty."

    def should_be_message_basket_empty(self):
        basket_empty = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY)
        assert basket_empty.get_attribute('href').split('/')[2] == "selenium1py.pythonanywhere.com", \
            "Empty basket message missing"
