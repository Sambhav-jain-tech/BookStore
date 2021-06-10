from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        Category.objects.create(name_c='django', slug='django')

    def test_Category_return_name(self):
        """ Test Category default model name"""
        data = Category.objects.get(name_c='django')
        self.assertEqual(str(data), 'django')


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name_c='django', slug='django')
        User.objects.create(username='admin')
        Product.objects.create(category_id=1, created_by_id=1, title='django beginners',
                               slug='django beginners', price='20.00', image='django')

    def test_product_return_title(self):
        """ Test Product default model title"""
        data = Product.objects.get(title='django beginners')
        self.assertEqual(str(data), 'django beginners')
