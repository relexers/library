from django.test import TestCase
from library.models import User
from .forms import NewUserForm
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


#Тесты urls
class URLTests(TestCase):
    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_api_homepage(self):
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)

    def test_api_readerpage(self):
        response = self.client.get('/api/reader/')
        self.assertEqual(response.status_code, 200)

    def test_api_bookpage(self):
        response = self.client.get('/api/book/')
        self.assertEqual(response.status_code, 200)

#Тест модели user
class ModelUserTest(TestCase):
    def create_user(self, name="testuser", id_passport="1234",
                        phone="1234", email="user@mail.com"):
        return User.objects.create(name=name, id_passport=id_passport,
                                    phone=phone, email=email)

    def test_user_creation(self):
        u = self.create_user()
        self.assertTrue(isinstance(u, User))
        self.assertEqual(u.__str__(), u.name)

#Тест формы
class FormTest(TestCase):
    #Тест наличия формы на странице
    def test_presence_form_on_the_hamepage(self):
        url = reverse('users')
        response = self.client.get(url)
        self.assertIn('form', response.context)
    #Тест валидности формы
    def test_is_valid_form(self):
        u = User.objects.create(name="testuser", id_passport="1234",
                            phone="1234", email="user@mail.com")
        data = {'name':u.name, 'id_passport': u.id_passport,
                'phone': u.phone, 'email': u.email}
        form = NewUserForm(data=data)
        self.assertTrue(form.is_valid())
    #Тест инвалидности формы)
    def test_invalid_form(self):
        u = User.objects.create(name="", id_passport="1234",
                            phone="1234", email="user@mail.com")
        data = {'name':u.name, 'id_passport': u.id_passport,
                'phone': u.phone, 'email': u.email}
        form = NewUserForm(data=data)
        self.assertFalse(form.is_valid())


# Тест создания пользователя
class UserTest(APITestCase):
    def test_create_user(self):
        url = reverse('users')
        u = User.objects.create(name="testuser", id_passport="1234",
                            phone="1234", email="user@mail.com")
        data = {'name':u.name, 'id_passport': u.id_passport,
                'phone': u.phone, 'email': u.email}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().email, "user@mail.com")



# Create your tests here.
