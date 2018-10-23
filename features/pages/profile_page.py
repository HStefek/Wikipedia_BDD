#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from selenium.webdriver.common.by import By
from browser import Browser

class ProfilePageLocator(object):

    HEADER_TEXT = (By.XPATH, "//h1")
    EDIT = (By.ID, "ca-edit")
    TEXT_FIELD = (By.ID, "wpTextbox1")
    SUBMIT_BUTTON = (By.ID, "wpSave")
    TEXT = (By.CLASS_NAME, "mw-parser-output")

class ProfilePage(Browser):

    def fill(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title
    
    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def fill_field(self, text):
        self.click_element(*ProfilePageLocator.EDIT)
        self.fill(text, *ProfilePageLocator.TEXT_FIELD)
        self.click_element(*ProfilePageLocator.SUBMIT_BUTTON)

    def check(self):
        return self.get_element(*ProfilePageLocator.TEXT).text

    def wipe(self):
        self.click_element(*ProfilePageLocator.EDIT)
        self.driver.find_element(*ProfilePageLocator.TEXT_FIELD).clear()
        self.click_element(*ProfilePageLocator.SUBMIT_BUTTON)


    
