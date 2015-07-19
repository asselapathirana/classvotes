from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest

from votes.views import home_page

class HomePageTest(TestCase):

    def test_url_root_resolves_to_home_page_function_in_view_module(self):
        root=resolve('/')
        self.assertEqual(root.func,home_page)

    def test_view_home_page_function_returns_essential_html(self):
        response=home_page(HttpRequest())
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>Classvotes: A simple classroom voting system</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
