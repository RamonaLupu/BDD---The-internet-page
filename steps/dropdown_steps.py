from behave import *

@when ('Home page: I click to Dropdown')
def step_impl(context):
    context.dropdown_object.go_to_dropdown_page

@then ('Dropdown page: I select Option 1 and i check if it is the first option')
def step_impl(context):
    context.dropdown_object.check_option

