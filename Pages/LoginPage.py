from selenium.webdriver.common.by import By
from Pages.BasePage import *

class LoginPage(Page):
    def __init__(self, driver):
        super(LoginPage, self).__init__(driver)

    email = (By.NAME, 'user-name')
    password = (By.NAME, 'password')
    submit_login = (By.NAME, 'login-button')

    # Função login
    def do_login(self, user, user_password):
            self.do_send_keys(self.email, user)
            self.do_send_keys(self.password, user_password)
            self.do_click(self.submit_login)