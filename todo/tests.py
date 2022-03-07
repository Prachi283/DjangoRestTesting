from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APIRequestFactory, force_authenticate
from todo.views import ListTodoAPIView, CreateTodoAPIView,UpdateTodoAPIView,DeleteTodoAPIView
from todo.models import Todo

class TodoAPITest(TestCase):

	def create_todo(self):
		sample_todo={'title':'Django','body':'some body'}
		response=self.client.post(reverse('todo_create'),sample_todo)
		return response

	def setUp(self):
		self.data={"title":"Some title","body":"some body","is_completed":True}
		Todo.objects.create(title="Django ORM Queries")
		self.factory = APIRequestFactory()

	def test_title_content(self):
		todo=Todo.objects.get(id=1)
		exp_object_name=f'{todo.title}'
		self.assertEquals(exp_object_name,'Django ORM Queries')

	def test_todo_list_view(self):
		response=self.client.get(reverse('todo_list'))
		self.assertEquals(response.status_code,200)
		self.assertContains(response,'Django ORM Queries')

	def test_get_data(self):
		list_url=reverse('todo_list')

		request=self.factory.get(list_url)
		response=ListTodoAPIView.as_view()(request)
		self.assertEqual(response.status_code,200)

	def test_post_data(self):
		create_url=reverse('todo_create')
		request=self.factory.post(create_url,data=self.data)
		response=CreateTodoAPIView.as_view()(request)
		self.assertEqual(response.status_code,201)

	def test_update_data(self):
		obj=self.create_todo()
		update_url=reverse("update_todo",kwargs={"body":obj.body})
		request=self.factory.put(update_url,data=self.data)
		response=UpdateTodoAPIView.as_view()(request,body=obj.body)
		self.assertEqual(response.status_code,201)
   
