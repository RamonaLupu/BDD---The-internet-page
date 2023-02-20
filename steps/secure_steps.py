
from behave import *

@when("Home page:I click to elem Form Authentication")
def step_impl(context):
    context.succes_object.go_login_page()


@when("Login page: Enter the correct user and password")
def step_impl(context):
    context.succes_object.insert_correct_user()
    context.succes_object.insert_correct_password()
    


@when("Login page: I click on the Login button")
def step_impl(context):
    context.succes_object.click_on_login_button()

@when("Secure page: I check if the success message is displayed")
def step_impl(context):
    context.succes_object.check_the_succes_message()

@then("Secure page: I click on the Logout button")
def step_impl(context):
    context.succes_object.click_logout_button()