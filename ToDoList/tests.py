from rest_framework.test import APITestCase
from rest_framework import status
from ToDoList.models import Post


class CreatePostTest(APITestCase):
    def test_post_create(self):
        url = '/api/posts/'
        data = {"title": "asd", "description": "sdfsdf"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_201_CREATED)


class GetPostTest(APITestCase):
    def setUp(self):
        self.post = Post.objects.create(title='TestCase',
                                        description='TestCase')

    def test_post_get(self):
        url = '/api/posts/' + str(self.post.id) + '/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class DeletePostTest(APITestCase):
    def setUp(self):
        self.post = Post.objects.create(title='TestCase',
                                        description='TestCase')

    def test_post_delete(self):
        url = '/api/posts/' + str(self.post.id) + '/'
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code,
                         status.HTTP_204_NO_CONTENT)
