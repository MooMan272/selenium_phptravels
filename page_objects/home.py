'''
Applies to the home page.
'''

import abc

from selenium.webdriver.common.by import By

from page_objects.base import BasePage, BaseElement
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

class BaseFeatured(BaseElement, metaclass=abc.ABCMeta):
    '''
    Abstract class representing a Featured Hotel, Tour, Car, or Offer.
    '''

    def __init__(self, element):
        '''
        Initialize self.

        Paramters
        ---------
        element : WebElement
            Element which this object represents.
        '''
        super().__init__()
        self.element = element
        # These are relative to self.element
        self.locator = {}
        self.locator['price'] = (By.CSS_SELECTOR, 'div.featured-price')

    @property
    def price(self):
        '''
        Returns price.
        '''
        return self.element.find_element(*self.locator['price']).text

    @property
    @abc.abstractmethod
    def title(self):
        '''
        Returns title.
        '''
        pass

class FeaturedOffer(BaseFeatured):
    '''
    Represents a Featured Offer.
    '''

    def __init__(self, element):
        '''
        Initialize self.

        Paramters
        ---------
        element : WebElement
            Element which this object represents.
        '''
        super().__init__(element)
        self.locator['title'] = (By.CSS_SELECTOR, 'div.featured-title')

    @property
    def title(self):
        '''
        Returns title.
        '''
        return self.element.find_element(*self.locator['title']).text
