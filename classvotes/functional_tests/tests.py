from selenium import webdriver
import unittest


class VisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_front_page_has_needed_tabs(self):
        # john goes to the webapp home page
        browser=webdriver.Firefox()
        browser.get('http://localhost:8000')

        # the title should have the word Classvotes
        assert 'Classvotes' in browser.title



