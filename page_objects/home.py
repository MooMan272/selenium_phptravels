'''
Applies to the home page.
'''

import abc

from selenium.webdriver.common.by import By

from page_objects.base import BasePage, LoadingElement
from page_objects.common import NavBar

class HomePageObject(BasePage):
    '''
    Applies to the home page.
    '''

    def __init__(self):
        super().__init__()
        self.url = 'http://www.phptravels.net/'
        self.locator = {}
        self.locator['featured_car_hotel_tour'] = (By.CSS_SELECTOR, 'div.bgwhite > div.container > div:nth-child(3) > div > a > div.featured')
        self.locator['featured_offer'] = (By.CSS_SELECTOR, 'div.offersbg > div.container > div > a > div.featured')
        self.locator['go_to_top'] = (By.CSS_SELECTOR, 'a.gotop')
        return

    def find_featured_car_hotel_tour_elements(self):
        '''
        Returns list of WebElements of each Featured Car/Hotel/Tour.
        '''
        return self.driver.find_elements(*self.locator['featured_car_hotel_tour'])

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

    def scroll_to_bottom(self):
        '''
        Scrolls to the bottom of the page.

        More specifically, scrolls to show the 'gotop' element. This scroll
        is instantaneous, so nothing in the middle of the page will 'load,'
        if it is something that loads dynamically.
        '''
        go_to_top = self.driver.find_element(*self.locator['go_to_top'])
        go_to_top.location_once_scrolled_into_view
        return

class BaseFeatured(LoadingElement, metaclass=abc.ABCMeta):
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
        self.locator['loading'] = (By.CSS_SELECTOR, 'div.load > img.img-responsive')
        self.locator['price'] = (By.CSS_SELECTOR, 'div.featured-price')

    def is_loaded(self):
        '''
        True if img src is not loading.svg.
        '''
        src_img = self.element.find_element(*self.locator['loading']).get_attribute('src')
        if src_img.endswith('loading.svg'): return False
        return True

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

class FeaturedCarHotelTour(BaseFeatured):
    '''
    Represents a Featured Car, Hotel, or Tour.
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
        self.locator['title'] = (By.CSS_SELECTOR, 'div.featured-title > div > div.strong')
        self.locator['location'] = (By.CSS_SELECTOR, 'div.featured-title > div > div:nth-child(7)')

    @property
    def location(self):
        '''
        Returns location.
        '''
        return self.element.find_element(*self.locator['location']).text

    @property
    def title(self):
        '''
        Returns title.
        '''
        return self.element.find_element(*self.locator['title']).text
