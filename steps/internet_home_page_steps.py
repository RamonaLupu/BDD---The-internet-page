from behave import *


@given('Home page: I am on The internet page')
def step_impl(context):
    context.home_page_object.navigate_to_homepage()


@when('Home page: I click to Form Authentication')
def step_impl(context):
    context.home_page_object.go_to_login_page()


@then('Home page: I go to the Login page')
def step_impl(context):
    context.home_page_object.check_url()
