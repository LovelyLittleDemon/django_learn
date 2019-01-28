from django.test import TestCase
from django.urls import resolve
from .views import home


# Create your tests here.


class HomeTest(TestCase):
    def test_home_view_status_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_home_url_resolvers_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)
