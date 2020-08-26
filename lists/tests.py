from django.test import TestCase
from django.urls import resolve
from lists.views import lists_page


class ListsPageTest(TestCase):
    def test_lists_url_resolves_to_home_page_view(self):
        found = resolve('/lists')
        self.assertEqual(found.func, lists_page)
