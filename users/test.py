from django.contrib.auth import get_user_model
from django.test import TestCase


class CustomerUserTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='dill',
            email='dia@gmail.com',
            password='testpass123'
        )
        self.assertEqual(user.username, 'dill')
        self.assertEqual(user.email, 'dia@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username='superadmin',
            email='super@email.com',
            password='super@1234'
        )
        self.assertEqual(user.username, 'superadmin')
        self.assertEqual(user.email, 'super@email.com')
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
