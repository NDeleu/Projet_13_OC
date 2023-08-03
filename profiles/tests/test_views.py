from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from profiles.models import Profile


class ProfileViewsTest(TestCase):
    def setUp(self):
        """
        Set up the necessary data for the tests,
            including creating a test user and profile.
        """
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Cityville")

    def test_index_view(self):
        """
        Test that the index view returns a response with status code 200,
            uses the correct template, and contains the username.
        """
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/index.html')
        self.assertContains(response, "testuser")

    def test_profile_view(self):
        """
        Test that the profile view for a valid username
            returns a response with status code 200, uses the correct template,
            and contains the username and favorite city.
        """
        response = self.client.get(reverse('profiles:profile', args=["testuser"]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertContains(response, "testuser")
        self.assertContains(response, "Cityville")

    def test_profile_view_invalid_username(self):
        """
        Test that the profile view for an invalid username
            returns a response that uses the error template.
        """
        invalid_username = "invaliduser"  # Using a non-existent username
        response = self.client.get(reverse('profiles:profile', args=[invalid_username]))
        self.assertTemplateUsed(response, 'error.html')
