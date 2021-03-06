from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FROM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.ID, "id_registration-email")
    REGISTER_PW1 = (By.ID, "id_registration-password1")
    REGISTER_PW2 = (By.ID, "id_registration-password2")
    REGISTER_BTN = (By.NAME, "registration_submit")

class ProductPageLocators:
    BTN_BASKET = (By.CLASS_NAME, "btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_page h1")
    NAME_PRODUCT_IN_BASKET = (By.CSS_SELECTOR, "[id='messages'] strong")
    PRICE_BOOK = (By.CSS_SELECTOR, "p.price_color")
    PRICE_BASKET = (By.CSS_SELECTOR, "[id='messages'] p strong")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "alertinner")

class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators:
    BASKET_LINK = (By.CSS_SELECTOR, ".btn-group a")
    BASKET_ITEMS = (By.CLASS_NAME, "basket-items")
    BASKET_EMPTY = (By.CSS_SELECTOR, "[id='content_inner'] a")
