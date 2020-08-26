from django.test import TestCase
from django.urls import resolve
from lists.views import lists_page
from django.http import HttpRequest


class ListsPageTest(TestCase):
    def test_lists_url_resolves_to_home_page_view(self):
        found = resolve('/lists')
        self.assertEqual(found.func, lists_page)

    def test_list_page_returns_correct_html(self):
        request = HttpRequest()
        response = lists_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<title>Joe\'s To-Do list</title>', html)
        self.assertTrue(html.endswith('</html>'))
