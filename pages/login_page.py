import time

from pages.base_page import Base_page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

class Login_page(Base_page):
    ELEM_FORM_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    USER = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    ERROR_LOGIN = (By.ID, 'flash')

    def navigate_to_login_page(self):
        self.chrom.find_element(*self.ELEM_FORM_AUTH).click()

    def insert_user(self):
        self.chrom.find_element(*self.USER).send_keys('ramo')

    def insert_password(self):
        self.chrom.find_element(*self.PASSWORD).send_keys('123')

    def click_on_the_login_button(self):
        self.chrom.find_element(*self.LOGIN_BUTTON).click()

    def check_the_error_message(self):
        assert self.chrom.find_element(*self.ERROR_LOGIN).is_displayed(), f'Error: The error message is not diplayed'