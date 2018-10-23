#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to the Croatian Wikipedia page')
def step_impl(context):
    context.croatian_page.navigate("https://hr.wikipedia.org/wiki/Glavna_stranica")
    assert_equal(context.croatian_page.get_page_title(), "Wikipedija")

@step('I go to "{user}" profile')
def step_impl(context, user):
    assert_true(context.croatian_page.find_user(user))
    context.croatian_page.go_to_user_page()

@step('I write "{text}"')
def step_impl(context, text):
    context.profile_page.fill_field(text)

@step('I verify if "{text}" is written')
def step_impl(context, text):
    assert_equal(context.profile_page.check(), text)

@step('I delete everything')
def step_impl(context):
    context.profile_page.wipe()