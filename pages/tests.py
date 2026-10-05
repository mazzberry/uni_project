from django.test import TestCase
from django.urls import reverse

# Create your tests here.

class testPages(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_aboutuspage(self):
        response = self.client.get(reverse('about-us'))
        self.assertEqual(response.status_code, 200)

    def test_aboutus_content(self):
        response = self.client.get(reverse('about-us'))
        self.assertContains(response, 'about-us')