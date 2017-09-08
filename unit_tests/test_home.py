'''
Unit tests for page_objects.common.
'''

import logging.config
import time

import pytest
from selenium import webdriver

import page_objects.base
from page_objects.home import HomePageObject, FeaturedOffer
import utils.logging_config
logging.config.dictConfig(utils.logging_config.config)

@pytest.fixture(scope='module')
def load_homepage():
    '''
    Setup fixture which loads the home page.
    '''
    page_objects.base.driver = webdriver.Chrome()
    homepage = HomePageObject()
    homepage.get(log_desc='home page')
    yield
    page_objects.base.driver.quit()
    return

class TestHomePage:
    '''
    Tests for HomePage.
    '''

    @pytest.fixture(scope='class')
    def home_page(self):
        '''
        Setup fixture which returns a HomePage object.
        '''
        return HomePageObject()

    def test_find_featured_offer_elements_returns_list_of_elements(self, load_homepage, home_page):
        '''
        Verify NavBar.find_link_elements() returns list of WebElements.
        '''
        featured_elements = home_page.find_featured_offer_elements()
        assert isinstance(featured_elements, list)
        assert len(featured_elements) > 0, "Empty list; can't verify items."
        for element in featured_elements:
            assert isinstance(element, webdriver.remote.webelement.WebElement)

class TestFeaturedOffer:
    '''
    Tests for FeaturedOffer.
    '''

    @pytest.fixture(scope='class')
    def featured_offer(self):
        '''
        Setup fixture which returns a FeaturedOffer object.
        '''
        home_page = HomePageObject()
        home_page.scroll_to_bottom()
        time.sleep(0.5)
        featured_elements = home_page.find_featured_offer_elements()
        # The last one is [probably] a Featured Offer.
        return FeaturedOffer(featured_elements[-1])

    def test_price(self, featured_offer):
        '''
        Verifies price string.
        '''
        price = featured_offer.price
        logging.debug("Price: '{}'.".format(price))
        assert price.startswith('USD $')

    def test_title(self, featured_offer):
        '''
        Verifies title string.
        '''
        title = featured_offer.title
        logging.debug("'Title: '{}'.".format(title))
        assert title != ''
