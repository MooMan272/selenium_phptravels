'''
Elements that appear on multiple pages.
'''

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

    def is_loaded(self):
        # True if itself is displayed.
        return self.element.is_displayed()
