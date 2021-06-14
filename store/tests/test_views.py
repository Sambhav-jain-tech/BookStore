from importlib import import_module
from unittest import skip

from django.conf import settings
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.test import Client, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import index


class TestViewResponses(TestCase):
    def setUp(self):
        Category.objects.create(name_c='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, created_by_id=1, title='django beginners',
                               slug='django-beginners', price='20.00', image='django')
        self.c = Client()

    def test_url_allowed_host(self):
        """
        test allowed host
        """
        response = self.c.get('/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_url(self):
        """
        test product response status
        """
        response = self.c.get(reverse('store:product_detail', args=['django-beginners']))
        self.assertEqual(response.status_code, 200)

    def test_category_detail_url(self):
        """
        test category response status
        """
        response = self.c.get(reverse('store:category_list', args=['django']))
        self.assertEqual(response.status_code, 200)

    def test_allowed_host(self):
        """
        test allowed hosts
        """
        response = self.c.get('/', http_host='127.0.0.1')
        self.assertEqual(response.status_code, 200)

    def test_home_html(self):
        request = HttpResponse()
        engine = import_module(settings.SESSION_ENGINE)
        request.session = engine.SessionStore() 
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> Home </title>', html)
        self.assertEqual(response.status_code,200)
