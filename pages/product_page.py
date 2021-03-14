from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_item_to_basket(self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

    def should_be_the_same_name(self):
        page_item_name = self.browser.find_element(*ProductPageLocators.PAGE_ITEM_NAME)
        basket_item_name = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_NAME)
        assert page_item_name.text == basket_item_name.text, "The names are not the same"
        
    def should_be_the_same_price(self):
        page_item_price = self.browser.find_element(*ProductPageLocators.PAGE_ITEM_PRICE)
        basket_item_price = self.browser.find_element(*ProductPageLocators.BASKET_ITEM_PRICE)
        assert page_item_price.text == basket_item_price.text, "The prices are not the same"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message should be disappeared"
    
