from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from votes.views import home_page, teacher_page

class HomePageTest(TestCase):

    def test_url_root_resolves_to_home_page_function_in_view_module(self):
        root=resolve('/')
        self.assertEqual(root.func,home_page)

    def test_view_home_page_function_returns_essential_html(self):
        response=home_page(HttpRequest())
        expected=render_to_string('home.html')
        self.assertEqual(response.content.decode(),expected)

class TeacherPageTest(TestCase):

    def test_url_teacher_resolves_to_teacher_page_function_in_view_module(self):
        teacherpage=resolve('/teacher/')
        self.assertEqual(teacherpage.func,teacher_page)

    def test_view_teacher_page_function_returns_essential_html(self):
        response=teacher_page(HttpRequest())
        expected=render_to_string('teacher_page.html')
        self.assertEqual(response.content.decode(),expected)

