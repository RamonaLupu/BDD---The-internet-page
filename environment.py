from browser import Browser
from pages.internet_home_page import Home_page
from pages.dropdown_page import Dropdown_page
from pages.login_page import Login_page
from pages.secure_page import Secure_page


def before_all(context):
    context.browser = Browser()
    context.home_page_object = Home_page()
    context.dropdown_object = Dropdown_page()
    context.error_object = Login_page()
    context.succes_object = Secure_page()



def after_all(context):
    context.browser.close()
