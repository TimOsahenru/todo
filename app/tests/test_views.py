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


class AllTodosViewTest(TestCase):
    def setUp(self):
        self.todos = [Todo.objects.create(title=f'todo title {i}') for i in range(3)]
        
        self.client = Client()


    def test_all_todos_view_endpoint(self):
        response = self.client.get(reverse('todo_list'))

        self.assertTemplateUsed(response, 'all_todos.html')
        self.assertIn('todos', response.context)

        for todo in self.todos:
            self.assertContains(response, todo.title)