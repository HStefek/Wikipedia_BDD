#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from selenium.webdriver.common.by import By
from browser import Browser

class LogInLocator(object):
    HEADER_TEXT = (By.XPATH, "//h1")
    USERNAME = (By.ID, "wpName1")
    PASSWORD = (By.ID, "wpPassword1")
    SUBMIT_BUTTON = (By.ID, "wpLoginAttempt")

class LogIn(Browser):

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

    def login(self, user, paswd):
        self.driver.find_element(*LogInLocator.USERNAME).clear()
        self.driver.find_element(*LogInLocator.PASSWORD).clear()
        self.fill(user, *LogInLocator.USERNAME)
        self.fill(paswd, *LogInLocator.PASSWORD)
        self.click_element(*LogInLocator.SUBMIT_BUTTON)

    