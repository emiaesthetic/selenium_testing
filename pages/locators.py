from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators:
    BTN_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_page h1")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "[id='messages'] strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, "[id='messages'] p strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")
