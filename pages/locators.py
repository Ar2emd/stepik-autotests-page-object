from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    PAGE_ITEM_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main > h1")
    BASKET_ITEM_NAME = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PAGE_ITEM_PRICE =(By.CSS_SELECTOR, "div.col-sm-6.product_main > p.price_color")
    BASKET_ITEM_PRICE =(By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages > div:nth-child(1)")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK =(By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")

class BasketPageLocators():
    BASKET_ITEMS =(By.CSS_SELECTOR, "#basket_formset > div.basket-items")
    EMPTY_BASKET_MESSAGE =(By.CSS_SELECTOR, "#content_inner > p")
    
