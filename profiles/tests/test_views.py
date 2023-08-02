from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


class ProfileViewsTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Cityville")

    def test_index_view(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, "testuser")

    def test_profile_view(self):
        response = self.client.get(reverse('profiles:profile', args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, "testuser")
        self.assertContains(response, "Cityville")

    def test_profile_view_invalid_username(self):
        invalid_username = "invaliduser"  # Using a non-existent username
        response = self.client.get(reverse('profiles:profile', args=[invalid_username]))
        self.assertTemplateUsed(response, 'error.html')
