import time

from pages.base_page import Base_page
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By


class Secure_page(Base_page):
    FORM_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    LOGIN_URL = 'https://the-internet.herokuapp.com/login'
    USER = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    SUCCES_MESSAGE = (By.ID, 'flash')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]/div/a/i')

    def go_login_page(self):
        self.chrom.find_element(*self.FORM_AUTH).click()

    def insert_correct_user(self):
        self.chrom.find_element(*self.USER).send_keys('tomsmith')

    def insert_correct_password(self):
        self.chrom.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')

    def click_on_login_button(self):
        self.chrom.find_element(*self.LOGIN_BUTTON).click()

    def check_the_succes_message(self):
        assert self.chrom.find_element(*self.SUCCES_MESSAGE).is_displayed(), f'Error: The error message is not diplayed'

    def click_logout_button(self):
        self.chrom.find_element(*self.LOGOUT_BUTTON).click()
        new_url = self.chrom.current_url
        assert new_url == self.LOGIN_URL, f'{new_url} is incorrect'

