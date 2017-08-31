'''
Applies to the home page.
'''

from selenium.webdriver.common.by import By

from page_objects.base import BasePage
from page_objects.common import NavBar

class HomePageObject(BasePage):
    '''
    Applies to the home page.
    '''

    def __init__(self):
        super().__init__()
        self.url = 'http://www.phptravels.net/'
        self.locator = {}
        self.locator['featured_offer'] = (By.CSS_SELECTOR, 'div.featured')
        return

    def find_featured_offer_elements(self):
        '''
        Returns list of WebElements of each Featured Offer.
        '''
        return self.driver.find_elements(*self.locator['featured_offer'])

    def is_loaded(self):
        '''
        True if the Nav is loaded.
        '''
        nav_bar = NavBar()
        return nav_bar.is_loaded()
