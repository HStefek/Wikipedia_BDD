#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase
 
from nose.tools import assert_equal, assert_true
from selenium.webdriver.common.by import By

@step('I navigate to the Wikipedia Home page')
def step_impl(context):
    context.home_page.navigate("https://www.wikipedia.org/")
    assert_equal(context.home_page.get_page_title(), "Wikipedia")

@step('I search for "{search_term}"')
def step_impl(context, search_term):
    context.home_page.search(search_term)

@step('I am taken to the Wikipedia Search Results page')
def step_impl(context):
    assert_equal(context.search_results_page.get_page_title(), "Python - Wikipedia")

@step('I see a search result "{search_result}"')
def step_impl(context, search_result):
    assert_true(context.search_results_page.find_search_result(search_result))
    context.search_results_page.open_search_result(search_result)