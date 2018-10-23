#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I change the language to "{lang}"')
def step_impl(context, lang):
    context.home_page.change_lang(lang)

@step('I am taken to the "{lang}" Wikipedia page')
def step_impl(context, lang):
    assert_equal(context.croatian_page.get_page_title(), "Wikipedija")


@step('I log in with credentials "{user}" \ "{paswd}"')
def step_impl(context, user, paswd):
    context.croatian_page.log_in()
    context.log_in.login(user, paswd)
    assert_true(context.croatian_page.find_user(user))

@step('I log out')
def step_impl(context):
    context.croatian_page.log_out()
