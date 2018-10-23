#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase


from selenium import webdriver
from browser import Browser
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage
from pages.croatian_page import CroatianPage
from pages.log_in import LogIn
from pages.profile_page import ProfilePage

def before_all(context):
    context.browser = Browser()
    context.home_page = HomePage()
    context.search_results_page = SearchResultsPage()
    context.croatian_page = CroatianPage()
    context.log_in = LogIn()
    context.profile_page = ProfilePage()

def after_all(context):
    context.browser.close()