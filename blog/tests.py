from django.test import TestCase
from django.core.urlresolvers import reverse

from rest_framework.test import APIClient
from rest_framework.test import APIRequestFactory

from blog.models import CustomUser, Post
from blog.views import PostList, AllPostList


class AuthTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='newauthor@gmail.com',
                                              password='123')
        self.client = APIClient()


    def test_auth_on_posts_works(self):
        # Doesn't work without login
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 401)

        #Works after login
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_doesnt_have_permissions_to_create_new_post(self):
        data = {'title': 'Some title', 'body': 'Some body'}

        response = self.client.post(reverse('posts'), data)
        self.assertEqual(Post.objects.count(), 0)

    def test_auth_on_all_posts_works(self):
        # Doesn't work without login
        response = self.client.get(reverse('all_posts'))
        self.assertEqual(response.status_code, 401)

        #Works after login
        self.client.force_authenticate(user=self.user)

        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)

    def test_shows_posts_on_user_profile(self):
        Post.objects.create(title='Title', body='Body', user=self.user)
        Post.objects.create(title='Test Title', body='Body', user=self.user)

        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('user'))
        self.assertEqual(response.data['posts'], ['Title', 'Test Title'])


class PostListTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='newauthor@gmail.com',
                                              password='123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_shows_only_current_user_posts(self):
        Post.objects.create(title='Title', body='Body', user=self.user)
        NewUser = CustomUser.objects.create(email='testauthor@gmail.com',
                                            password='123')

        Post.objects.create(title='Test Title', body='Body', user=NewUser)

        response = self.client.get(reverse('posts'))
        self.assertEqual(response.data['count'], 1)


    def test_creates_new_post(self):
        self.assertEqual(Post.objects.count(), 0)

        data = {'title': 'Some title', 'body': 'Some body'}

        response = self.client.post(reverse('posts'), data)
        self.assertEqual(Post.objects.count(), 1)

    def test_search_on_posts_works(self):
        Post.objects.create(title='Title', body='Body', user=self.user)
        Post.objects.create(title='Test Title', body='Body', user=self.user)

        # It finds 1 post with Test word
        response = self.client.get('/blog/posts/?search=Test')
        self.assertEqual(response.data['count'], 1)

        # It finds 2 posts with Body word
        response = self.client.get('/blog/posts/?search=Body')
        self.assertEqual(response.data['count'], 2)

class PostAllListTest(TestCase):

    def setUp(self):
        self.user = CustomUser.objects.create(email='newauthor@gmail.com',
                                              password='123')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)


    def test_shows_all_users_posts(self):
        Post.objects.create(title='Title', body='Body', user=self.user)
        NewUser = CustomUser.objects.create(email='testauthor@gmail.com',
                                            password='123')

        Post.objects.create(title='Test Title', body='Body', user=NewUser)

        response = self.client.get(reverse('all_posts'))
        self.assertEqual(response.data['count'], 2)


    def test_uses_page_pagination_fo_all_posts(self):
        Post.objects.create(title='Title', body='Body', user=self.user)
        NewUser = CustomUser.objects.create(email='testauthor@gmail.com',
                                            password='123')

        Post.objects.create(title='Test Title', body='Body', user=NewUser)

        response = self.client.get('/blog/posts/all/?page=1')
        self.assertEqual(len(response.data['results']), 2)


    def test_search_on_all_posts_works(self):
        Post.objects.create(title='Title', body='Body', user=self.user)
        NewUser = CustomUser.objects.create(email='testauthor@gmail.com',
                                            password='123')

        Post.objects.create(title='Test Title', body='Body', user=NewUser)

        # It finds 1 post with Test word
        response = self.client.get('/blog/posts/all/?search=Test')
        self.assertEqual(response.data['count'], 1)

        # It finds 2 posts with Body word
        response = self.client.get('/blog/posts/all/?search=Body')
        self.assertEqual(response.data['count'], 2)
