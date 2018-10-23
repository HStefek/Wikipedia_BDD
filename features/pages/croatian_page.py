#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from selenium.webdriver.common.by import By
from browser import Browser

class CroatianPageLocator(object):

    HEADER_TEXT = (By.XPATH, "//h1")
    LOG_IN = (By.ID, "pt-login")
    LOG_OUT = (By.ID, "pt-logout")
    USER_PAGE = (By.ID, "pt-userpage")

class CroatianPage(Browser):

    def get_element(self, *locator):
        return self.driver.find_element(*locator)

    def get_page_title(self):
        return self.driver.title
    
    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    def navigate(self, address):
        self.driver.get(address)

    def go_to_user_page(self):
        self.click_element(*CroatianPageLocator.USER_PAGE)

    def log_in(self):
        self.click_element(*CroatianPageLocator.LOG_IN)
    
    def log_out(self):
        self.click_element(*CroatianPageLocator.LOG_OUT)

    def find_user(self, user):
        return self.get_element(By.LINK_TEXT, user)