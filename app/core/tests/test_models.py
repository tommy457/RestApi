"""Tests for core app models"""

from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_success(self):
        """Test creating a user with email successfuly"""

        email = 'user@example.com'
        password = 'testing321'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
            )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_super_user(self):
        """test creating a super user"""
        user = get_user_model().objects.create_superuser(
            'testuser',
            'testing321'
            )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_new_user_with_email_raises_error(self):

        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'testing321')

    def test_new_user_email_is_normalized(self):

        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@ExamplE.Com', 'Test2@example.com'],
            ['TEST3@EXamPLE.com', 'TEST3@example.com'],
            ['test4@example.coM', 'test4@example.com'],
        ]
        for email, expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'testing321')
            self.assertEqual(user.email, expected)
