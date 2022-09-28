from selenium.webdriver.common.by import By
from Pages.BasePage import Page

class StorePage(Page):
    def __int__(self, driver):
        super(StorePage, self).__int__(driver)

    logo_store = (By.CLASS_NAME, '.app_logo')
    container_store = (By.CLASS_NAME, 'product_sort_container')
    order_lohi_store = (By.CSS_SELECTOR, '.product_sort_container [value~="lohi"] ')
    shopping_cart = (By.CLASS_NAME, 'shopping_cart_badge')

    sauce_labs_name = (By.CSS_SELECTOR, '.inventory_item:nth-child(1)  .inventory_item_name')
    sauce_labs_value = (By.CSS_SELECTOR, '.inventory_item:nth-child(1)  .inventory_item_price')
    sauce_add2cart = (By.ID, 'add-to-cart-sauce-labs-onesie')

    test_tshirt_name = (By.CSS_SELECTOR, '.inventory_item:nth-child(4)  .inventory_item_name')
    test_tshirt_value = (By.CSS_SELECTOR, '.inventory_item:nth-child(4)  .inventory_item_price')
    test_tshirt_add2cart = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')


    def select_low2high(self):
        self.do_click(self.order_lohi_store)

    def sauce_add_to_cart(self):
        self.do_click(self.sauce_add2cart)

    def test_tshirt_add_to_cart(self):
        self.do_click(self.test_tshirt_add2cart)

    def sauce_name(self):
        element = self.get_element_text(self.sauce_labs_name)
        return element

    def sauce_value(self):
        element = self.get_element_text(self.sauce_labs_value)
        element = element.replace('$', '')
        return element

    def ttat_tshirt_name(self):
        element = self.get_element_text(self.test_tshirt_name)
        return element

    def ttat_tshirt_value(self):
        element = self.get_element_text(self.test_tshirt_value)
        element = element.replace('$', '')
        return element

    def checkout_cart(self):
        self.do_click(self.shopping_cart)