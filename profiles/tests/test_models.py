from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import Profile


class ProfileModelTest(TestCase):
    def setUp(self):
        """
        Set up the necessary data for the tests,
            including creating a test user and profile.
        """
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.profile = Profile.objects.create(user=self.user, favorite_city="Cityville")

    def test_profile_str_representation(self):
        """
        Test that the string representation of a Profile instance
            is the username of the associated user.
        """
        self.assertEqual(str(self.profile), "testuser")
