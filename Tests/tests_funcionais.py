import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from Pages.LoginPage import LoginPage
from Pages.StorePage import StorePage
from Pages.CartPage import CartPage


class MyTestShop(unittest.TestCase):
    user = 'standard_user'
    user_password = 'secret_sauce'
    name = 'Ivan'
    last_name = 'Mendonca'
    cep = '01855750'

    def setUp(self):
        self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        self.driver.maximize_window()
        self.driver.get('https://www.saucedemo.com/')

    def test_login(self):
        login_page = LoginPage(self.driver)
        store_page = StorePage(self.driver)

        # Realizando o login
        login_page.do_login(self.user, self.user_password)
        elements = store_page.logo_store
        assert len(elements) > 0

    def test_order_low2high(self):
        login_page = LoginPage(self.driver)
        store_page = StorePage(self.driver)

        # Fazendo login
        login_page.do_login(self.user, self.user_password)

        # Alterar para Low to High
        store_page.select_low2high()
        time.sleep(2)
        elements = store_page.order_lohi_store
        assert len(elements) > 0


    def test_add_to_cart(self):
        login_page = LoginPage(self.driver)
        store_page = StorePage(self.driver)
        cart_page = CartPage(self.driver)

        # Fazendo login
        login_page.do_login(self.user, self.user_password)

        # Alterar para Low to High
        store_page.select_low2high()

        # Adicionar itens ao carrinho
        store_page.sauce_add_to_cart()
        sauce_store_name = store_page.sauce_name() # retornando nome
        sauce_store_value = store_page.sauce_value() # retornando valor

        store_page.test_tshirt_add_to_cart()
        ttat_store_name = store_page.ttat_tshirt_name() #retornando nome
        ttat_store_value = store_page.ttat_tshirt_value() #retornando o valor
        store_page.checkout_cart()

        # Comparando os itens do carrinho
        assert sauce_store_name == cart_page.sauce_name()
        assert sauce_store_value == cart_page.sauce_value()
        assert ttat_store_name == cart_page.ttat_tshirt_name()
        assert ttat_store_value == cart_page.ttat_tshirt_value()

    def test_complete_purchase(self):
        login_page = LoginPage(self.driver)
        store_page = StorePage(self.driver)
        cart_page = CartPage(self.driver)

        # Fazendo login
        login_page.do_login(self.user, self.user_password)

        # Alterar para Low to High
        store_page.select_low2high()

        # Adicionar itens ao carrinho
        store_page.sauce_add_to_cart()
        sauce_store_name = store_page.sauce_name()  # retornando nome
        sauce_store_value = store_page.sauce_value()  # retornando valor

        store_page.test_tshirt_add_to_cart()
        ttat_store_name = store_page.ttat_tshirt_name()  # retornando nome
        ttat_store_value = store_page.ttat_tshirt_value()  # retornando o valor
        store_page.checkout_cart()

        # Dando seguimento a compra
        cart_page.procedure_checkout()
        cart_page.preencher_dados_checkout(self.name, self.last_name, self.cep)
        total_itens = float(sauce_store_value) + float(ttat_store_value)
        assert total_itens == float(cart_page.itens_total())
        valor_total = float(total_itens) + float(cart_page.tax_total())
        assert valor_total == float(cart_page.total_somado())
        cart_page.finalizar()
        assert cart_page.comprado_sucesso() == 'THANK YOU FOR YOUR ORDER'

if __name__ == '__main__':
    unittest.main()