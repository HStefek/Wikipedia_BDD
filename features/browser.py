#Name: Wikipedia website test
#Author: Hrvoje Stefek
#Tools: Python, Behave, Nose, Selenium
#Note: Feel free to edit and reuse the code, it is made as tutorial and quick showcase

from selenium import webdriver

class Browser(object):

    driver = webdriver.Firefox(executable_path='path_to_geckodriver_file')
    driver.set_page_load_timeout(30)
    driver.implicitly_wait(30)
    driver.maximize_window()

    def close(context):
        context.driver.close()
