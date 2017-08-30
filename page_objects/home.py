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
        return

    def is_loaded(self):
        '''
        True if the Nav is loaded.
        '''
        nav_bar = NavBar()
        return nav_bar.is_loaded()
