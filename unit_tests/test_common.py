'''
Unit tests for page_objects.common.
'''

import logging.config

import pytest
from selenium import webdriver

import page_objects.base
from page_objects.home import HomePageObject
from page_objects.common import NavBar
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

class TestNavBar:
    '''
    Tests for NavBar.
    '''

    @pytest.fixture(scope='class')
    def nav_bar(self):
        '''
        Setup fixture which returns a NavBar object.
        '''
        return NavBar()

    def test_find_link_element_returns_element(self, load_homepage, nav_bar):
        '''
        Verify NavBar.find_link_element() returns WebElement.
        '''
        nav_link_element = nav_bar.find_link_element('home')
        assert isinstance(nav_link_element, webdriver.remote.webelement.WebElement)

    def test_find_link_elements_returns_list_of_elements(self, load_homepage, nav_bar):
        '''
        Verify NavBar.find_link_elements() returns list of WebElements.
        '''
        nav_link_elements = nav_bar.find_link_elements()
        assert isinstance(nav_link_elements, list)
        assert len(nav_link_elements) > 0, "Empty list; can't verify items."
        for element in nav_link_elements:
            assert isinstance(element, webdriver.remote.webelement.WebElement)
