import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pages.base_page import Base_page

class Dropdown_page(Base_page):
    ELEM_DROPDOWN = (By.XPATH, '//*[@id="content"]/ul/li[11]/a')
    DROPDOWN_OPT = (By.XPATH, '//*[@id="dropdown"]')

    def go_to_dropdown_page(self):
        self.wait_and_click_element(*self.ELEM_DROPDOWN)
    def check_option(self):
        option_dropdown = Select(self.chrom.find_element(*self.DROPDOWN_OPT))
        option = option_dropdown.select_by_visible_text('Option 1')
        time.sleep(5)
        assert option_dropdown.first_selected_option == option, f'Error: {option} is not the first option.'
