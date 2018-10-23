#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from selenium.webdriver.common.by import By
from browser import Browser

class SearchResultsPageLocator(object):

    HEADER_TEXT = (By.XPATH, "//h1")

class SearchResultsPage(Browser):

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title

    def find_search_result(self, search_result):
        return self.get_element(By.LINK_TEXT, search_result)

    def open_search_result(self, search_result):
        self.get_element(By.LINK_TEXT, search_result).click()