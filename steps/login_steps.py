from behave import *

@when("Home page: I go to the Login page")
def step_impl(context):
    context.error_object.navigate_to_login_page()


@when("Login page: Enter the incorrect user and password")
def step_impl(context):
    context.error_object.insert_user()
    context.error_object.insert_password()


@when("Login page: Click on the Login button")
def step_impl(context):
    context.error_object.click_on_the_login_button()

@then("Login page: The error message must be diplayed")
def step_impl(context):
    context.error_object.check_the_error_message()