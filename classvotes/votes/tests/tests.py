from django.core.urlresolvers import resolve
from django.test import TestCase
from votes.views import home_page

class HomePageTest(TestCase):

    def test_url_root_resolves_to_home_page_function_in_view_module(self):
        root=resolve('/')
        self.assertEqual(root.func,home_page)


