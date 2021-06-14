from django.contrib.auth.models import User
from django.test import TestCase
from store.models import Category, Product
from django.urls import reverse

class TestBasketView(TestCase):
    def setUp(self):
        User.objects.create(username='admin')
        Category.objects.create(name_c='django', slug='django')
        Product.objects.create(category_id=1, created_by_id=1, title='django beginners',
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, created_by_id=1, title='django intermediate',
                               slug='django-beginners', price='20.00', image='django')
        Product.objects.create(category_id=1, created_by_id=1, title='django advanced',
                               slug='django-beginners', price='20.00', image='django')

        self.client.post(
            reverse('basket:basket_add'),{'productid': 1, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.client.post(
            reverse('basket:basket_add'),{'productid': 2, 'productqty': 2, 'action': 'post'}, xhr=True)

    def test_basket_url(self):
        """
        test homepage response status
        """
        response = self.client.get(reverse('basket:basket_summary'))
        self.assertEqual(response.status_code,200)

    def test_basket_add(self):
        """
        test basket_add view
        """
        response = self.client.post(reverse('basket:basket_add'), {'productid': 3, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 4})
        response = self.client.post(reverse('basket:basket_add'),{'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 3})

    def test_basket_delete(self):
        """
        test basket_delete view
        """
        response = self.client.post(reverse('basket:basket_delete'), {'productid': 2, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 1, 'subtotal': '20.00'})

    def test_basket_update(self):
        """
        test basket_update view
        """
        response = self.client.post(reverse('basket:basket_update'), {'productid': 2, 'productqty': 1, 'action': 'post'}, xhr=True)
        self.assertEqual(response.json(), {'qty': 2, 'subtotal': '40.00'})
