'''
Contains definitions for all base classes.

Attributes
----------
driver : WebDriver
    This variable is for the WebDriver object. It must be set before any
    Page Objects can be instantiated. It will effectively be a global
    variable, but should cause no problems assuming no test requires multiple
    browser instances.

Some approaches choose to treat BasePage and BaseElement as unrelated
objects. I choose to disregard this for the sake of simplicity.

BaseElement is a simple extension of a WebDriver object. It can represent
any element on the page, big (e.g the entire page) or small.

BasePage extends BaseElement _minimally._ It defines a URL attribute (so
think of a BasePage representing a single given URL) and a method to directly
load that URL.

Some pages are small and simple enough to use one BasePage to represent the
entire page. Two very common general situations warrant multiple objects:
* A page is too big/complex and gets "bigger than your head."
* An element (big or small) with a given internal structure appears in
  multiple areas. Could be on different pages (e.g. a menu nav) or on
  the same page (e.g. HTML list items).
    * In such a case, you'll need to tell it how to find the specific
      WebElement you want to reference. It could be "I already found
      the WebElement, here you go" or "look for the WebElement with this
      text."

In such cases, one BasePage and one or more BaseElements will be used in
conjunction.
'''

from abc import ABCMeta, abstractmethod
import logging
import time

driver = None

class Loading(metaclass=ABCMeta):
    '''
    An element that has a loading/loaded state.
    '''

    @abstractmethod
    def is_loaded(self):
        '''
        Checks to see if the element is loaded.

        Returns
        -------
        bool
        '''
        pass

    def wait_for_load(self, time_limit=5.0, log_desc='Object'):
        '''
        Waits for the element to load.

        Parameters
        ----------
        time_limit : integer, float, optional
            Max time to wait for the element to load.
        log_desc : str, optional
            Description of the element, written to logs.

        Returns
        -------
        None

        Raises
        ------
        Exception
            If time limit is exceeded.
        '''
        log_desc = log_desc.title()
        end_time = time.time() + time_limit
        while time.time() < end_time:
            time.sleep(0.5)
            if self.is_loaded():
                logging.info('{} loaded.'.format(log_desc))
                return
            logging.debug('{} not loaded yet.'.format(log_desc))
        log_str = '{} did not load.'.format(log_desc)
        logging.error(log_str)
        raise Exception(log_str)

class BaseElement:
    '''
    Extends a WebDriver object.
    '''

    def __init__(self):
        if driver == None:
            raise Exception('page_objects.base.driver variable must be set to the WebDriver before any Page or Element Objects can be instantiated.')
        self.driver = driver

class LoadingElement(BaseElement, Loading):
    '''
    A BaseElement that has a loading/loaded state.
    '''
    pass

class BasePage(LoadingElement):
    '''
    Represents an "entire page," i.e. a single URL.

    Some elements have a loading state; some don't. All pages need to have a
    way to indicate the page has loaded, hence the distinction with
    elements, but not pages.

    Attributes
    ----------
    url : str
        URL which this object represents.
    '''

    def __init__(self):
        super().__init__()
        self.url = None
        return

    def get(self, time_limit=5.0, log_desc='Page'):
        '''
        Directly opens the page, then waits for the page to load.

        Parameters
        ----------
        time_limit : integer, float, optional
            Max time to wait for the element to load. The actual wait time
            is longer than this, since the driver.get() method d
        log_desc : str, optional
            Description of the element, written to logs.
        '''
        if self.url is None:
            log_str = 'This class has no URL attribute defined.'
            logging.error(log_str)
            raise Exception(log_str)
        log_desc = log_desc.title()
        logging.info('Directly loading {}.'.format(log_desc))
        self.driver.get(self.url)
        self.wait_for_load(log_desc=log_desc, time_limit=time_limit)
        return
