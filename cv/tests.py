from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from .models import Cv


class TestViews(TestCase):
    def setUp(self):
        Cv.objects.create(content='<html><body>hello</body></html>')
        self.user = User.objects.create_superuser(username='mrsuper',
                                                  email='mrsuperr@super.super',
                                                  password='password')

    def test_cv_page_uses_cv_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv.html')

    def test_page_displays_first_cv(self):
        response = self.client.get('/cv/')
        self.assertContains(response, 'hello')

    def test_cv_edit_anonymous_user(self):
        response = self.client.get('/cv/edit/')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')

    def test_cv_edit_user_uses_edit_template(self):
        self.client.login(username='mrsuper', password='password')
        response = self.client.get('/cv/edit/')

        self.assertTemplateUsed(response, 'cv-edit.html')
