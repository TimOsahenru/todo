from django.test import TestCase, Client
from django.urls import reverse
from app import views
from app.models import Todo


class CreateTodoViewTest(TestCase):
    def setUp(self):
        self.client = Client()


    def test_get_request_displays_form(self):

        response = self.client.post(reverse('create_todo'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')


    def test_create_todo_page_redirects(self):

        data = {
            'title': '10 push ups',
            'description': 'Do 10 push ups everyday',
        }

        response = self.client.post(reverse('create_todo'), data)

        self.assertEqual(response.status_code, 302)