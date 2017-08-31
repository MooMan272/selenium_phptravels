'''
Elements that appear on multiple pages.
'''

import logging

from selenium.webdriver.common.by import By

from page_objects.base import LoadingElement

class NavBar(LoadingElement):
    '''
    Main nav bar which appears at the top of every page.
    '''

    def __init__(self):
        super().__init__()
        self.locator = {}

        # Find the element which this object will represent.
        self.locator['nav'] = (By.CSS_SELECTOR, 'nav.navbar-default')
        self.element = self.driver.find_element(*self.locator['nav'])

        # These are relative to locator['nav']
        self.locator['link'] = (By.CSS_SELECTOR, 'li')
        return

    def find_link_element(self, text):
        '''
        Returns WebElement of link with the given text.
        '''
        nav_elements = self.find_link_elements()
        for element in nav_elements:
            if element.text.lower() == text.lower():
                return element
        log_str = "Nav Link '{}' not found.".format(text)
        logging.error(log_str)
        raise Exception

    def find_link_elements(self):
        '''
        Returns list of WebElements of each link.
        '''
        return self.element.find_elements(*self.locator['link'])

    def is_loaded(self):
        # True if itself is displayed.
        return self.element.is_displayed()
