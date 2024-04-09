from django.test import TestCase, RequestFactory
from .models import Product, Feedback
from .views import feedback_form
from .forms import FeedbackForm


class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name='Test Product')

    def test_product_creation(self):
        product = Product.objects.get(name='Test Product')
        self.assertIsInstance(product, Product)
        self.assertEqual(product.__str__(), 'Test Product')


class FeedbackFormViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.product = Product.objects.create(name='Test Product')

    def test_feedback_form_view(self):
        request = self.factory.post('/feedback_form/', {
            'customer_name': 'Test Customer',
            'email': 'test@example.com',
            'product': self.product.id,
            'details': 'Test details',
            'happy': True,
        })
        response = feedback_form(request)
        self.assertEqual(response.status_code, 200)

        feedback = Feedback.objects.first()
        self.assertEqual(feedback.customer_name, 'Test Customer')
