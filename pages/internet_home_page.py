import time
from pages.base_page import Base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

class Home_page(Base_page):
    ELEM_FORM_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    LOGIN_URL = 'https://the-internet.herokuapp.com/login'

    def navigate_to_homepage(self):
        self.chrom.get('https://the-internet.herokuapp.com/')

    def go_to_login_page(self):
        self.chrom.find_element(*self.ELEM_FORM_AUTH).click()

    def check_url(self):
        actual_url = self.chrom.current_url
        expected_url = self.LOGIN_URL
        assert actual_url == expected_url, f'Error: The url is not correct! Actual url is {actual_url} and expected url is {expected_url}'







