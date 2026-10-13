from django.test import TestCase
from django.contrib.auth import get_user_model
from django.shortcuts import reverse

from .models import Post

User = get_user_model()


# Create your tests here.

class Blog_Post_test(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(username='test-user1')
        cls.post1 = Post.objects.create(
            title='test title',
            author=cls.user,
            text='salam in yek matn test hast',
            status=Post.STATUS_CHOICES[0][0],  # published
        )
        cls.post2 = Post.objects.create(
            title='post2 draft',
            author=cls.user,
            text='lorem impsum post2',
            status=Post.STATUS_CHOICES[1][0],  # draft
        )

    def test_post_model_str(self):
        post = self.post1
        self.assertEqual(str(post), post.title)

    def test_post_detail(self):
        self.assertEqual(self.post1.title, 'test title')
        self.assertEqual(self.post1.text, 'salam in yek matn test hast')

    def test_postlist_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_postlist_url_byname(self):
        response = self.client.get(reverse('blog-page'))
        self.assertEqual(response.status_code, 200)

    def test_title_postlist_view(self):
        response = self.client.get(reverse('blog-page'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_on_detail_page(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_postdetail_url_byname(self):
        response = self.client.get(reverse('post-detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_404_if_does_n_exist(self):
        response = self.client.get(reverse('post-detail', args=[99999999999999]))
        self.assertEqual(response.status_code, 404)

    def test_draft_post_not_show_postlist(self):
        response = self.client.get(reverse('blog-page'))
        self.assertContains(response, self.post1.title)
        self.assertNotContains(response, self.post2.title)

    def test_create_post_requires_login(self):
        response = self.client.post(reverse('new-post'), {
            'title': 'some title',
            'text': 'some test text',
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response.url)

    def test_update_post_requires_login(self):
        response = self.client.post(reverse('update-post', args=[self.post1.id]), {
            'title': 'some title',
            'text': 'some test text',
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response.url)

    def test_delete_post_requires_login(self):
        response = self.client.post(reverse('delete-post', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login', response.url)

    def test_create_post_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('new-post'), {
            'title': 'some title',
            'text': 'some test text',
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        last_post = Post.objects.last()
        self.assertEqual(last_post.title, 'some title')
        self.assertEqual(last_post.text, 'some test text')
        self.assertEqual(last_post.author, self.user)

    def test_update_post_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('update-post', args=[self.post2.id]), {
            'title': ' post 2 some title updated ',
            'text': 'this text updated',
            'status': 'pub',
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.last().title, 'post 2 some title updated')
        self.assertEqual(Post.objects.last().text, 'this text updated')

    def test_delete_post_view(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete-post', args=[self.post1.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Post.objects.filter(id=self.post1.id).count(), 0)