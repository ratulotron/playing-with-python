from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page


# Functional test
class HomePageTest(TestCase):
    
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')
        # self.assertTemplateUsed(response, 'wrong.html')


# class SmokeTest(TestCase):

#     def test_bad_maths(self):
#         self.assertEqual(1+1,3)
