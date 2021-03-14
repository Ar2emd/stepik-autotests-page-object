from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    
    def should_not_be_items_in_the_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), "Item is in the basket, but should not be"

    def should_be_empty_basket_message(self):
        assert "Your basket is empty" in self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, "There should be a message about empty basket"
        
    
