from selenium.webdriver.common.by import By
from Pages.BasePage import Page

class CartPage(Page):
    def __int__(self, driver):
        super(CartPage, self).__int__(driver)

    tatt_tshirt = (By.CSS_SELECTOR, '#item_3_title_link .inventory_item_name')
    test_tshirt_value = (By.CSS_SELECTOR,
                         '#cart_contents_container > div > div.cart_list > div:nth-child(4) > div.cart_item_label > div.item_pricebar > div')
    sauce_labs_name = (By.CSS_SELECTOR, '#item_2_title_link .inventory_item_name')
    sauce_labs_value = (By.CSS_SELECTOR,
                        '#cart_contents_container > div > div.cart_list > div:nth-child(3) > div.cart_item_label > div.item_pricebar > div')
    checkout_button = (By.ID, 'checkout')
    first_name = (By.ID, 'first-name')
    last_name = (By.ID, 'last-name')
    postal_code = (By.ID, 'postal-code')
    continue_button = (By.ID, 'continue')
    item_total = (By.CLASS_NAME, 'summary_subtotal_label')
    tax =  (By.CLASS_NAME, 'summary_tax_label')
    total_compra = (By.CLASS_NAME, 'summary_total_label')
    finish_button = (By.ID, 'finish')
    finish_purchase = (By.CLASS_NAME, 'complete-header')

    def sauce_name(self):
        element = self.get_element_text(self.sauce_labs_name)
        return element

    def sauce_value(self):
        element = self.get_element_text(self.sauce_labs_value)
        element = element.replace('$', '')
        return element

    def ttat_tshirt_name(self):
        element = self.get_element_text(self.tatt_tshirt)
        return element

    def ttat_tshirt_value(self):
        element = self.get_element_text(self.test_tshirt_value)
        element = element.replace('$', '')
        return element

    def procedure_checkout(self):
        self.do_click(self.checkout_button)

    def preencher_dados_checkout(self, name, last_name, cep):
        self.do_send_keys(self.first_name, name)
        self.do_send_keys(self.last_name, last_name)
        self.do_send_keys(self.postal_code, cep)
        self.do_click(self.continue_button)

    def itens_total(self):
        element = self.get_element_text(self.item_total)
        element = element.replace('Item total: $', '')
        return element

    def tax_total(self):
        element = self.get_element_text(self.tax)
        element = element.replace('Tax: $', '')
        return element

    def total_somado(self):
        element = self.get_element_text(self.total_compra)
        element = element.replace('Total: $', '')
        return element

    def finalizar(self):
        self.do_click(self.finish_button)

    def comprado_sucesso(self):
        element = self.get_element_text(self.finish_purchase)
        return element