'''
Unit tests for page_objects.common.
'''

import logging.config
import time

import pytest
from selenium import webdriver

import page_objects.base
from page_objects.home import HomePageObject, FeaturedCarHotelTour, FeaturedOffer
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

class TestFeaturedCarHotelTour:
    '''
    Tests for FeaturedCarHotelTour.
    '''

    @pytest.fixture(scope='class')
    def featured_car_hotel_tour(self):
        '''
        Setup fixture which returns a list of FeaturedCarHotelTour objects.
        '''
        home_page = HomePageObject()
        home_page.scroll_to_bottom()
        time.sleep(0.5)
        featured_elements = home_page.find_featured_car_hotel_tour_elements()
        # Convert to list of FeaturedCarHotelTour objects
        featured_car_hotel_tour_objects = []
        for i in featured_elements:
            featured_car_hotel_tour_objects.append(FeaturedCarHotelTour(i))
        return featured_car_hotel_tour_objects

    def test_location(self, load_homepage, featured_car_hotel_tour):
        '''
        Verifies location string.
        '''
        for featured_cht in featured_car_hotel_tour:
            location = featured_cht.location
            logging.debug("Location: '{}'.".format(location))
            assert location != ''

    def test_price(self, load_homepage, featured_car_hotel_tour):
        '''
        Verifies price string.
        '''
        for featured_cht in featured_car_hotel_tour:
            price = featured_cht.price
            logging.debug("Price: '{}'.".format(price))
            assert price.startswith('USD $')

    def test_title(self, load_homepage, featured_car_hotel_tour):
        '''
        Verifies title string.
        '''
        for featured_cht in featured_car_hotel_tour:
            title = featured_cht.title
            logging.debug("'Title: '{}'.".format(title))
            assert title != ''

class TestFeaturedOffer:
    '''
    Tests for FeaturedOffer.
    '''

    @pytest.fixture(scope='class')
    def featured_offers(self):
        '''
        Setup fixture which returns a list of FeaturedOffer objects.
        '''
        home_page = HomePageObject()
        home_page.scroll_to_bottom()
        time.sleep(0.5)
        featured_offer_elements = home_page.find_featured_offer_elements()
        # Convert featured_offer_elements to list of FeaturedOffer objects
        featured_offer_objects = []
        for i in featured_offer_elements:
            featured_offer_objects.append(FeaturedOffer(i))
        return featured_offer_objects

    def test_price(self, load_homepage, featured_offers):
        '''
        Verifies price string.
        '''
        for featured_offer in featured_offers:
            price = featured_offer.price
            logging.debug("Price: '{}'.".format(price))
            assert price.startswith('USD $')

    def test_title(self, load_homepage, featured_offers):
        '''
        Verifies title string.
        '''
        for featured_offer in featured_offers:
            title = featured_offer.title
            logging.debug("'Title: '{}'.".format(title))
            assert title != ''
