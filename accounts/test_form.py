from django.test import TestCase
from .forms import UserLoginForm, UserRegistrationForm
from django.contrib.auth.models import User
# Create your tests here.

class TestAccountsForms(TestCase):#we use the name of a class in another class to get all the methods of it.
     
     def test_login_form(self):
         form = UserLoginForm({
            'username': 'admin',
            'password': 'thing12345',
         })
         self.assertTrue(form.is_valid())
         
     def test_login_password_required(self):
         form= UserLoginForm({'username': 'admin'})
         self.assertFalse(form.is_valid())
         print(form.errors['password'])
         
     def test_login_username_required(self):
         form= UserLoginForm({'password': 'thing12345'})
         self.assertFalse(form.is_valid())
         print(form.errors['username'])
         
     def test_registration_form(self):
          form = UserRegistrationForm({
             'username': 'admin',
             'email': 'admin@example.com',
             'password1': 'thing12345',
             'password2': 'thing12345',
         })
          self.assertTrue(form.is_valid())
          
     def test_registration_passwords_must_match(self):
         form = UserRegistrationForm({
             'username': 'admin',
             'email': 'admin@example.com',
             'password1': 'thing12345',
             'password2': 'thing123456'
             })
         self.assertFalse(form.is_valid())
         self.assertEqual(form.errors['password2'], ['Passwords do not match'])
         
     def test_registration_email_must_be_unique(self):
         User.objects.create_user(
             username= 'testuser',
             email='admin@example.com')
         
         form = UserRegistrationForm({
             'username': 'admin',
             'email': 'admin@example.com',
             'password1': 'thing12345',
             'password2': 'thing12345',
             })
         self.assertFalse(form.is_valid())
         self.assertEqual(form.errors['email'], ['Email addresses must be unique.'])
            