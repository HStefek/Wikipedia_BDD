#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from selenium.webdriver.common.by import By
from browser import Browser

class HomePageLocator(object):
    HEADER_TEXT = (By.XPATH, "//h1")
    SEARCH_FIELD = (By.ID, "searchInput")
    LANG_SELCTOR = (By.ID, "js-lang-list-button")
    SUBMIT_BUTTON = (By.TAG_NAME, "button")

class HomePage(Browser):

    def get_element(self, *locator):
        return self.driver.find_element(*locator)
    
    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def get_page_title(self):
        return self.driver.title
    
    def search(self, search_term):
        self.fill(search_term, *HomePageLocator.SEARCH_FIELD)
        self.click_element(*HomePageLocator.SUBMIT_BUTTON)

    def change_lang(self, lang):
        self.click_element(*HomePageLocator.LANG_SELCTOR)
        self.get_element(By.LINK_TEXT, lang).click()