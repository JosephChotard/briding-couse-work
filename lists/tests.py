from django.test import TestCase
from django.urls import resolve
from lists.views import lists_page


class ListsPageTest(TestCase):
    def test_list_page_uses_list_home_template(self):
        response = self.client.get('/lists')
        self.assertTemplateUsed(response, 'lists/home.html')

    def test_page_can_save_a_POST_request(self):
        response = self.client.post(
            '/lists', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.content.decode())
        self.assertTemplateUsed(response, 'lists/home.html')
