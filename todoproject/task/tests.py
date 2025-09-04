from django.test import TestCase
from .models import Task, Category
from django.contrib.auth import get_user_model
from django.urls import reverse


User = get_user_model()

class TaskModelTest(TestCase):

    def setUp(self):
        self.u1 = User.objects.create_user(username='a', password='p')
        Task.objects.create(title='test', owner=self.u1,
                            description='test message',
                            )

    def test_task_content(self):
        self.client.login(username='a', password='p')
        resp = self.client.get(reverse('task:task_list'))
        self.assertContains(resp, 'test')


class HomePageViewTest(TestCase):

    def setUp(self):
        self.u1 = User.objects.create_user(username='a', password='p')
        Task.objects.create(title='test', owner=self.u1,
                            description='test message',
                            )

    def test_view_url_exist(self):
        resp = self.client.get('/')
        self.assertEquals(resp.status_code, 200)

    def test_view_url_task(self):
        resp = self.client.get(reverse('task:task_list'))
        self.assertEquals(resp.status_code, 200)

